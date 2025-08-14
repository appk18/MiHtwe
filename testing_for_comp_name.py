import os
import sys
import re
import cv2
import numpy as np
import pytesseract
import fitz  # PyMuPDF
from PyPDF2 import PdfReader, PdfWriter

# === Setup paths ===
if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

tesseract_path = os.path.join(base_path, 'tesseract_portable_windows', 'tesseract.exe')
pytesseract.pytesseract.tesseract_cmd = tesseract_path

pdf_path = os.path.join(base_path, 'TSI_POD_20200620.pdf')  
sorted_pdf_path = os.path.join(base_path, 'Sorted_Output.pdf')
debug_dir = os.path.join(base_path, "debug_pages")
os.makedirs(debug_dir, exist_ok=True)

# === Preprocess image for OCR ===
def preprocess_image_for_ocr(cv_img):
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.convertScaleAbs(gray, alpha=1.5, beta=0)
    gray = cv2.medianBlur(gray, 3)

    # Adaptive threshold
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 31, 2
    )

    # --- Automatic rotation correction using Tesseract ---
    try:
        osd = pytesseract.image_to_osd(thresh)
        rotate_match = re.search(r'Rotate: (\d+)', osd)
        if rotate_match:
            rotate_angle = int(rotate_match.group(1))
            if rotate_angle != 0:
                (h, w) = thresh.shape
                M = cv2.getRotationMatrix2D((w//2, h//2), -rotate_angle, 1.0)
                thresh = cv2.warpAffine(
                    thresh, M, (w, h),
                    flags=cv2.INTER_CUBIC,
                    borderMode=cv2.BORDER_REPLICATE
                )
    except Exception as e:
        print("OSD rotation detection failed:", e)

    # --- Fallback deskew with minAreaRect ---
    coords = np.column_stack(np.where(thresh > 0))
    if coords.size > 0:
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle

        (h, w) = thresh.shape
        M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])
        new_w = int((h*sin) + (w*cos))
        new_h = int((h*cos) + (w*sin))
        M[0,2] += (new_w/2) - w//2
        M[1,2] += (new_h/2) - h//2

        thresh = cv2.warpAffine(
            thresh, M, (new_w, new_h),
            flags=cv2.INTER_CUBIC,
            borderMode=cv2.BORDER_REPLICATE
        )

    return thresh

# === OCR wrapper ===
def ocr_text_from_image(image):
    configs = [
        '--psm 1 --oem 3',  # Full page as single block
        '--psm 3 --oem 3',
        '--psm 6 --oem 3 -c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-/."'
    ]
    best_text = ""
    for config in configs:
        try:
            text = pytesseract.image_to_string(image, config=config).strip()
            if len(text) > len(best_text):
                best_text = text
        except Exception:
            continue
    return [l.strip() for l in best_text.splitlines() if l.strip()]

# === Extract DO number & company ===
def extract_info(lines):
    do_no = "UNKNOWN"
    company = "UNKNOWN"

    do_pattern = re.compile(
        r'\b(?:DO|MO|TST)\s*[\.\-:,#]?\s*(?:No\.?|Number)?\s*[:\-]?\s*([A-Z0-9\/\-]{4,})',
        re.IGNORECASE
    )

    do_line_index = -1
    for idx, line in enumerate(lines):
        match = do_pattern.search(line)
        if match:
            do_no = match.group(1)
            do_line_index = idx
            break

    if do_line_index != -1 and do_line_index + 1 < len(lines):
        company = lines[do_line_index + 1]

    return do_no, company

# === Extract page number ===
def extract_page_no(lines):
    text = "\n".join(lines)
    match = re.search(r'Page\s*(?:No\.?)?\s*(\d+)', text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    match = re.search(r'\b(\d{1,3})\s+of\s+\d{1,3}\b', text)
    if match:
        return int(match.group(1))
    return None

# === Render PDF page to OpenCV image ===
def render_page_to_image(doc, page_number, dpi=400):
    page = doc.load_page(page_number)
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom).prerotate(page.rotation)
    pix = page.get_pixmap(matrix=mat, alpha=False)

    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    if pix.n == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    return img

# === Main ===
def main(pdf_path):
    print(f"Reading PDF: {pdf_path}")
    doc = fitz.open(pdf_path)
    page_count = doc.page_count
    print(f"Total pages: {page_count}")

    page_data = []
    reader = PdfReader(pdf_path)

    for i in range(page_count):
        print(f"\n--- Processing Page {i+1}/{page_count} ---")
        page = doc.load_page(i)
        text = page.get_text().strip()

        if text:
            # Page has real text, use it directly
            lines = [l.strip() for l in text.splitlines() if l.strip()]
        else:
            # Page is image, use OCR
            raw_img = render_page_to_image(doc, i, dpi=500)
            preprocessed_img = preprocess_image_for_ocr(raw_img)
            cv2.imwrite(os.path.join(debug_dir, f"page_{i+1}_preprocessed.png"), preprocessed_img)
            lines = ocr_text_from_image(preprocessed_img)

        print("Generated lines:", lines, "...\n")

        do_no, company = extract_info(lines)
        page_no = extract_page_no(lines)

        page_data.append({
            "index": i,
            "do_no": do_no,
            "company": company,
            "page_no": page_no
        })

        print(f"[Extracted] DO No   : {do_no}")
        print(f"[Extracted] Company : {company}")
        print(f"[Extracted] Page No : {page_no}")

    # Sort pages
    sorted_pages = sorted(
        page_data,
        key=lambda x: (
            re.sub(r'\W+', '', x["company"].split()[0]).lower() if x["company"] else "",
            x["do_no"]
        )
    )

    # Save sorted PDF
    writer = PdfWriter()
    for page in sorted_pages:
        writer.add_page(reader.pages[page["index"]])
    with open(sorted_pdf_path, "wb") as f:
        writer.write(f)

    print(f"\nSorted PDF saved to: {sorted_pdf_path}")
    print(f"Debug images saved in: {debug_dir}")

if __name__ == "__main__":
    main(pdf_path)
