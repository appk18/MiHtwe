from pdf2image import convert_from_path
# import cv2
import numpy as np

# pages = convert_from_path('TSI_POD_20200620.pdf', poppler_path=r'D:\5.APPK\Personal\PJ\Release-24.08.0-0\poppler-24.08.0\Library\bin')

# total_stamp_count = 0

# for i, page in enumerate(pages):
#     img = np.array(page)
#     img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#     # Blue color range (tweak if needed)
#     lower_blue = np.array([90, 50, 50])
#     upper_blue = np.array([130, 255, 255])
#     mask = cv2.inRange(hsv, lower_blue, upper_blue)

#     # Optional: noise removal
#     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
#     mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((3,3), np.uint8))

#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


#     stamp_count_page = 0
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 700:
#             stamp_count_page += 1

#     total_stamp_count += stamp_count_page
#     print(f"Page {i+1} - stamps found: {stamp_count_page}")



# from pdf2image import convert_from_path
# import cv2
# import numpy as np

# pages = convert_from_path(
#     'TSI_POD_20200620.pdf',
#     poppler_path=r'C:\Project\Release-24.08.0-0\poppler-24.08.0\Library\bin'
# )

# total_circle_count = 0

# for i, page in enumerate(pages):
#     img = np.array(page)
#     img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

#     lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#     l, a, b = cv2.split(lab)
#     clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
#     cl = clahe.apply(l)
#     enhanced_lab = cv2.merge((cl, a, b))
#     img = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     lower_blue = np.array([90, 50, 50])
#     upper_blue = np.array([130, 255, 255])
#     mask = cv2.inRange(hsv, lower_blue, upper_blue)

#     kernel = np.ones((3, 3), np.uint8)
#     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#     mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     circle_count = 0  # count circles per page
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area < 300:
#             continue

#         perimeter = cv2.arcLength(cnt, True)
#         approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)

#         if len(approx) >= 8:
#             circle_count += 1
#             cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)

#     total_circle_count += circle_count
#     print(f"Page {i + 1} - Stamp found: {circle_count}")






# from pdf2image import convert_from_path
# import cv2
# import numpy as np
# import os

# pdf_path = input("Enter the full path of the PDF file: ")

# if not os.path.isfile(pdf_path):
#     print("File not found.")
#     exit()

# # Set your poppler path
# poppler_path = r'D:\5.APPK\Personal\Lab\Release-24.08.0-0\poppler-24.08.0\Library\bin'

# pages = convert_from_path(pdf_path, poppler_path=poppler_path)

# total_circle_count = 0

# for i, page in enumerate(pages):
#     img = np.array(page)
#     img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

#     lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#     l, a, b = cv2.split(lab)
#     clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
#     cl = clahe.apply(l)
#     enhanced_lab = cv2.merge((cl, a, b))
#     img = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     lower_blue = np.array([90, 50, 50])
#     upper_blue = np.array([130, 255, 255])
#     mask = cv2.inRange(hsv, lower_blue, upper_blue)

#     kernel = np.ones((3, 3), np.uint8)
#     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#     mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     circle_count = 0
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area < 300:
#             continue
#         perimeter = cv2.arcLength(cnt, True)
#         approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
#         if len(approx) >= 8:
#             circle_count += 1

#     total_circle_count += circle_count
#     print(f"Page {i + 1} - Stamp found: {circle_count}")

# input("Press Enter to exit...")



# import os
# from pdf2image import convert_from_path
# import easyocr
# from PyPDF2 import PdfReader, PdfWriter

# def get_pdf_path():
#     path = input("Enter full path to your PDF file: ").strip('"')
#     if not os.path.isfile(path):
#         print("❌ File not found!")
#         return None
#     return path

# def process_pdf(pdf_path, poppler_path):
#     images = convert_from_path(pdf_path, poppler_path=poppler_path)
#     reader = easyocr.Reader(['en'])
#     stamp_data = []

#     for idx, img in enumerate(images):
#         results = reader.readtext(np.array(img))
#         stamp_texts = [text[1] for text in results if len(text[1].strip()) > 2]
#         print(f"Page {idx + 1} → Stamps: {stamp_texts}")
#         stamp_data.append((idx, sorted(stamp_texts)))

#     sorted_pages = sorted(stamp_data, key=lambda x: x[1][0].lower() if x[1] else "zzz")

#     # sorted_pages 
#     return sorted_pages

# def save_sorted_pdf(original_pdf, sorted_data, output_file):
#     reader = PdfReader(original_pdf)
#     writer = PdfWriter()
#     for idx, _ in sorted_data:
#         writer.add_page(reader.pages[idx])
#     with open(output_file, "wb") as f:
#         writer.write(f)
#     print(f"✅ Sorted PDF saved as: {output_file}")

# if __name__ == "__main__":
#     import numpy as np
#     import cv2

#     poppler_path = r"D:\5.APPK\Personal\Lab\Release-24.08.0-0\poppler-24.08.0\Library\bin"  
#     pdf_path = get_pdf_path()

#     if pdf_path:
#         sorted_pages = process_pdf(pdf_path, poppler_path)
#         output_pdf = os.path.splitext(pdf_path)[0] + "_sorted.pdf"
#         save_sorted_pdf(pdf_path, sorted_pages, output_pdf)




# # This is the final reading stamp

# from pdf2image import convert_from_path
# import cv2
# import numpy as np
# import os
# from colorama import Fore, Style, init
# from tabulate import tabulate

# # Initialize colorama
# init(autoreset=True)

# pdf_path = input("Enter the full path of the PDF file: ")

# if not os.path.isfile(pdf_path):
#     print("File not found.")
#     exit()

# # Extract the document name
# doc_name = os.path.basename(pdf_path)

# # Define Poppler path
# poppler_path = r'D:\5.APPK\Personal\Lab\Release-24.08.0-0\poppler-24.08.0\Library\bin'
# pages = convert_from_path(pdf_path, poppler_path=poppler_path)

# # Table data to collect
# table_data = []
# pass_count = 0
# fail_count = 0

# # Process each page
# for i, page in enumerate(pages):
#     img = np.array(page)
#     img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

#     lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#     l, a, b = cv2.split(lab)
#     clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
#     cl = clahe.apply(l)
#     enhanced_lab = cv2.merge((cl, a, b))
#     img = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     lower_blue = np.array([90, 50, 50])
#     upper_blue = np.array([130, 255, 255])
#     mask = cv2.inRange(hsv, lower_blue, upper_blue)

#     kernel = np.ones((3, 3), np.uint8)
#     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#     mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     circle_count = 0
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area < 300:
#             continue
#         perimeter = cv2.arcLength(cnt, True)
#         approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
#         if len(approx) >= 8:
#             circle_count += 1

#     # Determine status
#     if circle_count >= 3:
#         status_colored = Fore.GREEN + "PASS" + Style.RESET_ALL
#         pass_count += 1
#     else:
#         status_colored = Fore.RED + "FAIL" + Style.RESET_ALL
#         fail_count += 1

#     # Append formatted row
#     table_data.append([i + 1, circle_count, status_colored])

# # Display Results
# print("=" * 60)
# print(f"\nStamp Verification for \"{doc_name}\"")
# print("=" * 60)
# headers = ["Page", "No. of Stamps", "Status"]
# print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", colalign=("center", "center", "center")))
# print("=" * 60)

# # Summary Section
# print("\nSUMMARY")
# print(f"Total No. of Pages : {len(pages)}")
# print(Fore.GREEN + f"PASS : {pass_count}")
# print(Fore.RED + f"FAIL : {fail_count}")
# print("=" * 60)


# if fail_count > 0:
#     failing_pages = [str(row[0]) for row in table_data if "FAIL" in row[2]]
#     print(Fore.YELLOW + "\nPages with FAILED stamp check: " + ", ".join(failing_pages) + Style.RESET_ALL)
#     print("Please open the PDF and navigate to the above pages to review the stamps.")

# input("\nPress Enter to exit...")


# To Try 

# import easyocr
# from pdf2image import convert_from_path
# import numpy as np
# import cv2
# import os

# # ======= USER SETTINGS =======
# PDF_PATH = 'yourfile.pdf'  # Replace with your PDF file
# POPPLER_PATH = r'C:\path\to\poppler\bin'  # <-- Set this if you're on Windows
# SAVE_OUTPUT_IMAGE = True
# # ==============================

# # Convert PDF to image
# print("Converting PDF to image...")
# pages = convert_from_path(PDF_PATH, poppler_path=POPPLER_PATH)
# image = np.array(pages[0])  # Use the first page only

# # Convert to OpenCV format
# image_cv = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# # Initialize OCR
# print("Running OCR...")
# reader = easyocr.Reader(['en'])
# results = reader.readtext(image)

# # Search for stamp keywords
# keywords = ['warehouse', 'transporter', 'customer']
# found_stamps = []

# for (bbox, text, confidence) in results:
#     lower_text = text.lower()
#     for keyword in keywords:
#         if keyword in lower_text:
#             print(f"[FOUND] {keyword.title()} Stamp: '{text}' (Confidence: {confidence:.2f})")
#             found_stamps.append((keyword.title(), bbox))
#             # Draw rectangle around detected stamp
#             pts = np.array(bbox, dtype=np.int32)
#             cv2.polylines(image_cv, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
#             cv2.putText(image_cv, keyword.title(), tuple(pts[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

# # Save or display result
# if SAVE_OUTPUT_IMAGE:
#     output_path = os.path.splitext(PDF_PATH)[0] + '_detected.jpg'
#     cv2.imwrite(output_path, image_cv)
#     print(f"Saved output to: {output_path}")

# # Optional: show image (press any key to close)
# cv2.imshow("Detected Stamps", image_cv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




# For UI

# import tkinter as tk
# from tkinter import filedialog, messagebox, ttk
# from pdf2image import convert_from_path
# import cv2
# import numpy as np
# import os

# # poppler_path = r'D:\5.APPK\Personal\Lab\Release-24.08.0-0\poppler-24.08.0\Library\bin'

# import os
# import sys

# if getattr(sys, 'frozen', False):
#     # If the application is run as a bundle (i.e., .exe)
#     base_path = os.path.dirname(sys.executable)
# else:
#     # If run as a normal Python script
#     base_path = os.path.dirname(os.path.abspath(__file__))

# poppler_path = os.path.join(base_path, 'Release-24.08.0-0', 'poppler-24.08.0', 'Library', 'bin')

# class StampCheckerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("PDF Stamp Checker")
#         self.root.geometry("860x720")
#         self.root.resizable(False, False)
#         self.pdf_paths = []
#         self.build_gui()

#     def build_gui(self):
#         tk.Label(self.root, text="PDF Stamp Checker", font=("Segoe UI", 16, "bold")).pack(pady=10)

#         file_frame = tk.Frame(self.root)
#         file_frame.pack(pady=5)

#         self.file_entry = tk.Entry(file_frame, width=75, font=("Segoe UI", 12))
#         self.file_entry.pack(side=tk.LEFT, padx=5, pady=3)

#         browse_btn = tk.Button(
#             file_frame, text="Browse", command=self.browse_file, width=12,
#             bg="#0078D4", fg="white", font=("Segoe UI", 10, "bold"),
#             relief="flat", activebackground="#005A9E", activeforeground="white"
#         )
#         browse_btn.pack(side=tk.LEFT, padx=5)

#         self.start_btn = tk.Button(
#             self.root, text="Start Checking", command=self.run_check, width=20,
#             bg="#06920D", fg="white", font=("Segoe UI", 10, "bold"),
#             state=tk.DISABLED  # disabled initially
#         )
#         self.start_btn.pack(pady=10)

#         self.file_label = tk.Label(self.root, text="No file loaded", font=("Segoe UI", 12, "italic"), fg="gray")
#         self.file_label.pack(pady=(5, 0))

#         tree_frame = tk.Frame(self.root)
#         tree_frame.pack(padx=10, pady=10, fill='both', expand=True)

#         columns = ("page", "stamps", "result")
#         self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
#         for col in columns:
#             self.tree.heading(col, text=col.title(), command=lambda c=col: self.sort_treeview(c, False))
#         self.tree.column("page", width=200, anchor='center')
#         self.tree.column("stamps", width=150, anchor='center')
#         self.tree.column("result", width=120, anchor='center')
#         self.tree.pack(side=tk.LEFT, fill='both', expand=True)

#         scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
#         self.tree.configure(yscroll=scrollbar.set)
#         scrollbar.pack(side=tk.RIGHT, fill='y')

#         style = ttk.Style()
#         style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))
#         style.configure("Treeview", font=("Consolas", 11), background="white", foreground="black", fieldbackground="white")

#         self.tree.tag_configure("pass", foreground="green", font=("Consolas", 11, "bold"))
#         self.tree.tag_configure("fail", foreground="red", font=("Consolas", 11, "bold"))
#         self.tree.tag_configure("oddrow", background="#f9f9f9")
#         self.tree.tag_configure("evenrow", background="white")
#         self.tree.tag_configure("fileheader", background="#d9d9d9", font=("Segoe UI", 12, "bold"))
#         self.tree.tag_configure("summary", background="#e1e1e1", font=("Segoe UI", 11, "italic"), foreground="blue")
#         self.tree.tag_configure("separator", background="#ffffff", font=("Consolas", 11), foreground="#888888")

#         self.summary_label = tk.Label(self.root, text="", font=("Segoe UI", 12, "bold"), fg="navy", justify="left", anchor="w")
#         self.summary_label.pack(fill='x', padx=10, pady=(0, 10))

#         self.failed_pages_lbl = tk.Label(self.root, text="", font=("Segoe UI", 11, "bold"), fg="red", justify="left")
#         self.failed_pages_lbl.pack(pady=5, anchor="w")

#         # Footer frame for copyright and version info
#         footer_frame = tk.Frame(self.root)
#         footer_frame.pack(side=tk.BOTTOM, fill='x', pady=5)
#         copyright_label = tk.Label(
#             footer_frame, text="© 2025 MadebyCodeNest. All rights reserved.",
#             font=("Segoe UI", 9), fg="gray"
#         )
#         copyright_label.pack()

#     def browse_file(self):
#         file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
#         if file_paths:
#             self.pdf_paths = file_paths
#             display_text = ", ".join([os.path.basename(fp) for fp in file_paths])
#             self.file_entry.delete(0, tk.END)
#             self.file_entry.insert(0, display_text)
#             self.file_label.config(text=f"Loaded files: {display_text}", fg="black")
#             self.start_btn.config(state=tk.NORMAL)  # enable start button

#     # Add sort functionality to Treeview columns
#     def sort_treeview(self, col, reverse):
#         data = [(self.tree.set(k, col), k) for k in self.tree.get_children('')]
#         try:
#             data.sort(key=lambda t: int(t[0]), reverse=reverse)
#         except ValueError:
#             data.sort(reverse=reverse)
#         for index, (val, k) in enumerate(data):
#             self.tree.move(k, '', index)
#         self.tree.heading(col, command=lambda: self.sort_treeview(col, not reverse))

#     def count_circles(self, img):
#         hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#         lower_blue = np.array([90, 50, 50])
#         upper_blue = np.array([130, 255, 255])
#         mask = cv2.inRange(hsv, lower_blue, upper_blue)
#         kernel = np.ones((3, 3), np.uint8)
#         mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#         mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
#         contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         count = 0
#         for cnt in contours:
#             area = cv2.contourArea(cnt)
#             if area < 300:
#                 continue
#             perimeter = cv2.arcLength(cnt, True)
#             approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
#             if len(approx) >= 8:
#                 count += 1
#         return count


#     def run_check(self):
#         self.tree.delete(*self.tree.get_children())
#         self.failed_pages_lbl.config(text="")
#         self.summary_label.config(text="")

#         if not self.pdf_paths:
#             messagebox.showerror("Error", "Please select at least one PDF file.")
#             return

#         total_files = len(self.pdf_paths)
#         total_pages = 0
#         total_pass = 0
#         total_fail = 0
#         overall_failed_pages = []

#         for file_index, path in enumerate(self.pdf_paths):
#             if not os.path.isfile(path):
#                 messagebox.showwarning("Warning", f"File not found: {path}")
#                 continue

#             try:
#                 pages = convert_from_path(path, poppler_path=poppler_path)
#             except Exception as e:
#                 messagebox.showerror("Error", f"Error loading PDF {os.path.basename(path)}:\n{e}")
#                 continue

#             # Insert file header row
#             file_tag = f"fileheader{file_index}"
#             self.tree.insert("", "end", values=(f"File: {os.path.basename(path)}", "", ""), tags=("fileheader",))

#             file_pass = 0
#             file_fail = 0
#             file_failed_pages = []

#             for i, page in enumerate(pages):
#                 img = np.array(page)
#                 img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#                 lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#                 l, a, b = cv2.split(lab)
#                 clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
#                 cl = clahe.apply(l)
#                 enhanced_lab = cv2.merge((cl, a, b))
#                 img = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
#                 circle_count = self.count_circles(img)

#                 is_pass = circle_count >= 3
#                 result_text = "PASS" if is_pass else "FAIL"
#                 tag_result = "pass" if is_pass else "fail"
#                 tag_row = "oddrow" if i % 2 == 0 else "evenrow"

#                 display_count = min(circle_count, 3)
#                 self.tree.insert("", "end", values=(f"Page {i + 1}", display_count, result_text), tags=(tag_result, tag_row))

#                 if is_pass:
#                     file_pass += 1
#                 else:
#                     file_fail += 1
#                     file_failed_pages.append(str(i + 1))

#             # Summary row per file
#             summary_values = (
#                 f"Summary for {os.path.basename(path)}",
#                 f"Pages Passed: {file_pass}",
#                 f"Pages Failed: {file_fail}"
#             )
#             self.tree.insert("", "end", values=summary_values, tags=("summary",))

#             # Add separator line after file
#             self.tree.insert("", "end", values=("", "", ""), tags=("separator",))

#             # Accumulate totals
#             total_pages += len(pages)
#             total_pass += file_pass
#             total_fail += file_fail
#             if file_fail > 0:
#                 overall_failed_pages.append(f"{os.path.basename(path)} (Pages: {', '.join(file_failed_pages)})")

#         # Display overall summary
#         overall_summary = (
#             f"Total Files: {total_files}    |    "
#             f"Total Pages: {total_pages}    |    "
#             f"Total Passed: {total_pass}    |    "
#             f"Total Failed: {total_fail}"
#         )
#         self.summary_label.config(text=overall_summary)

#         if overall_failed_pages:
#             failed_text = "Failed Pages:\n" + "\n".join(overall_failed_pages)
#             self.failed_pages_lbl.config(text=failed_text, fg="red")
#         else:
#             self.failed_pages_lbl.config(text="All pages passed successfully.", fg="green")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = StampCheckerApp(root)
#     root.mainloop()


# import sys
# import os
# import numpy as np
# import cv2
# from pdf2image import convert_from_path
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QPushButton, QLabel, QLineEdit,
#     QVBoxLayout, QHBoxLayout, QFileDialog, QTableWidget,
#     QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView,
#     QProgressBar
# )
# from PyQt5.QtCore import Qt, QThread, pyqtSignal
# from PyQt5.QtGui import QColor, QCursor


# # Set poppler path
# if getattr(sys, 'frozen', False):
#     base_path = os.path.dirname(sys.executable)
# else:
#     base_path = os.path.dirname(os.path.abspath(__file__))

# poppler_path = os.path.join(base_path, 'Release-24.08.0-0', 'poppler-24.08.0', 'Library', 'bin')


# # Button styling function
# def style_button(button, color="#0078D4", hover_color="#005A9E", font_size=12):
#     button.setStyleSheet(f"""
#         QPushButton {{
#             background-color: {color};
#             color: white;
#             font-weight: bold;
#             font-size: {font_size}px;
#             border-radius: 6px;
#             padding: 6px 12px;
#         }}
#         QPushButton:hover {{
#             background-color: {hover_color};
#         }}
#         QPushButton:pressed {{
#             background-color: #004B87;
#         }}
#         QPushButton:disabled {{
#             background-color: gray;
#             color: white;
#         }}
#     """)
#     button.setCursor(QCursor(Qt.PointingHandCursor))


# class CheckWorker(QThread):
#     progress_update = pyqtSignal(int)
#     add_table_row = pyqtSignal(str, str, str, bool, bool, object, object)
#     update_summary = pyqtSignal(str, str)
#     done = pyqtSignal()

#     def __init__(self, pdf_paths, poppler_path):
#         super().__init__()
#         self.pdf_paths = pdf_paths
#         self.poppler_path = poppler_path
    

#     def count_circles(self, img):
#         hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#         lower_blue = np.array([90, 50, 50])
#         upper_blue = np.array([130, 255, 255])
#         mask = cv2.inRange(hsv, lower_blue, upper_blue)
#         kernel = np.ones((3, 3), np.uint8)
#         mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#         mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
#         contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         count = 0
#         for cnt in contours:
#             area = cv2.contourArea(cnt)
#             if area < 300:
#                 continue
#             perimeter = cv2.arcLength(cnt, True)
#             approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
#             if len(approx) >= 8:
#                 count += 1
#         return count

#     def run(self):
#         total_files = len(self.pdf_paths)
#         total_pages = 0
#         total_pass = 0
#         total_fail = 0
#         overall_failed_pages = []

#         for path in self.pdf_paths:
#             if not os.path.isfile(path):
#                 continue

#             try:
#                 pages = convert_from_path(path, poppler_path=self.poppler_path)
#             except Exception:
#                 continue

#             self.add_table_row.emit(f"File: {os.path.basename(path)}", "", "", True, False, QColor("#000000"), QColor("#d9d9d9"))

#             file_pass = 0
#             file_fail = 0
#             file_failed_pages = []

#             for i, page in enumerate(pages):
#                 img = np.array(page)
#                 img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#                 lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#                 l, a, b = cv2.split(lab)
#                 clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
#                 cl = clahe.apply(l)
#                 enhanced_lab = cv2.merge((cl, a, b))
#                 img = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
#                 circle_count = self.count_circles(img)


#                 is_pass = circle_count >= 3
#                 result_text = "PASS" if is_pass else "FAIL"
#                 display_count = min(circle_count, 3)
#                 fg_color = QColor("green") if is_pass else QColor("red")

#                 self.add_table_row.emit(f"Page {i + 1}", str(display_count), result_text, False, False, fg_color, None)

#                 if is_pass:
#                     file_pass += 1
#                 else:
#                     file_fail += 1
#                     file_failed_pages.append(str(i + 1))

#             self.add_table_row.emit(
#                 f"Summary for {os.path.basename(path)}",
#                 f"Pages Passed: {file_pass}",
#                 f"Pages Failed: {file_fail}",
#                 True, True, QColor("blue"), QColor("#e1e1e1")
#             )

#             self.add_table_row.emit("", "", "", False, False, None, QColor("#ffffff"))

#             total_pages += len(pages)
#             total_pass += file_pass
#             total_fail += file_fail
#             if file_fail > 0:
#                 overall_failed_pages.append(f"{os.path.basename(path)} (Pages: {', '.join(file_failed_pages)})")

#         overall_summary = (
#             f"Total Files: {total_files}    |    "
#             f"Total Pages: {total_pages}    |    "
#             f"Total Passed: {total_pass}    |    "
#             f"Total Failed: {total_fail}"
#         )
#         failed_text = "All pages passed successfully." if not overall_failed_pages else "Failed Pages:\n" + "\n".join(overall_failed_pages)

#         self.update_summary.emit(overall_summary, failed_text)
#         self.done.emit()


# class StampCheckerApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PDF Stamp Checker")
#         self.setGeometry(150, 100, 1000, 720)
#         self.pdf_paths = []
#         self.init_ui()

#     def init_ui(self):
#         layout = QVBoxLayout()

#         title_label = QLabel("PDF Stamp Checker")
#         title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
#         title_label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(title_label)

#         file_layout = QHBoxLayout()
#         self.file_entry = QLineEdit()
#         self.file_entry.setReadOnly(True)
#         self.file_entry.setMinimumHeight(30)
#         font = self.file_entry.font()
#         font.setPointSize(10)
#         self.file_entry.setFont(font)
#         file_layout.addWidget(self.file_entry)

#         browse_btn = QPushButton("Browse")
#         style_button(browse_btn)
#         browse_btn.setFixedWidth(100)
#         browse_btn.setToolTip("Select one or more PDF files to check")
#         browse_btn.clicked.connect(self.browse_files)
#         file_layout.addWidget(browse_btn)
#         layout.addLayout(file_layout)

#         self.start_btn = QPushButton("Start Checking")
#         self.start_btn.setEnabled(False)
#         self.start_btn.setFixedWidth(150)
#         style_button(self.start_btn, color="#06920D", hover_color="#04730B")
#         self.start_btn.setToolTip("Start checking selected files")
#         self.start_btn.clicked.connect(self.run_check)

#         btn_layout = QHBoxLayout()
#         btn_layout.addStretch()
#         btn_layout.addWidget(self.start_btn)
#         btn_layout.addStretch()
#         layout.addLayout(btn_layout)

#         self.file_label = QLabel("No file loaded")
#         self.file_label.setStyleSheet("font-style: italic; color: gray;")
#         layout.addWidget(self.file_label)

#         self.table = QTableWidget()
#         self.table.setColumnCount(3)
#         self.table.setHorizontalHeaderLabels(["Page", "Stamps Found", "Result"])
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
#         header = self.table.horizontalHeader()
#         font = header.font()
#         font.setBold(True)
#         header.setFont(font)
#         layout.addWidget(self.table)

#         self.progress_bar = QProgressBar()
#         self.progress_bar.setRange(0, 0)
#         self.progress_bar.setVisible(False)
#         layout.addWidget(self.progress_bar)

#         self.summary_label = QLabel("")
#         self.summary_label.setStyleSheet("font-weight: bold; color: navy;")
#         layout.addWidget(self.summary_label)

#         self.failed_pages_label = QLabel("")
#         self.failed_pages_label.setStyleSheet("font-weight: bold; color: red;")
#         layout.addWidget(self.failed_pages_label)

#         footer_label = QLabel("© 2025 MadebyCodeNest. All rights reserved.")
#         footer_label.setStyleSheet("color: gray; font-size: 10px;")
#         footer_label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(footer_label)

#         self.setLayout(layout)

#     def browse_files(self):
#         files, _ = QFileDialog.getOpenFileNames(self, "Select PDF files", "", "PDF Files (*.pdf)")
#         if files:
#             self.pdf_paths = files
#             display_text = ", ".join([os.path.basename(f) for f in files])
#             self.file_entry.setText(display_text)
#             self.file_label.setText(f"Loaded files: {display_text}")
#             self.file_label.setStyleSheet("color: black;")
#             self.start_btn.setEnabled(True)

#     def run_check(self):
#         if not self.pdf_paths:
#             QMessageBox.warning(self, "Error", "Please select at least one PDF file.")
#             return

#         self.table.setRowCount(0)
#         self.failed_pages_label.setText("")
#         self.summary_label.setText("")
#         self.start_btn.setEnabled(False)
#         self.progress_bar.setVisible(True)

#         self.worker = CheckWorker(self.pdf_paths, poppler_path)
#         self.worker.add_table_row.connect(self.insert_table_row)
#         self.worker.update_summary.connect(self.update_summary_labels)
#         self.worker.done.connect(self.on_check_finished)
#         self.worker.start()

#     def on_check_finished(self):
#         self.progress_bar.setVisible(False)
#         self.start_btn.setEnabled(True)

#     def insert_table_row(self, col1, col2, col3, bold=False, italic=False, fg_color=None, bg_color=None):
#         row_idx = self.table.rowCount()
#         self.table.insertRow(row_idx)
#         item1 = QTableWidgetItem(col1)
#         item2 = QTableWidgetItem(col2)
#         item3 = QTableWidgetItem(col3)
#         font = item1.font()
#         font.setPointSize(10)
#         font.setBold(bold)
#         font.setItalic(italic)
#         for item in (item1, item2, item3):
#             item.setFont(font)
#             item.setForeground(fg_color or QColor(30, 30, 30))
#             if bg_color:
#                 item.setBackground(bg_color)
#         self.table.setItem(row_idx, 0, item1)
#         self.table.setItem(row_idx, 1, item2)
#         self.table.setItem(row_idx, 2, item3)

#     def update_summary_labels(self, summary_text, failed_text):
#         self.summary_label.setText(summary_text)
#         self.failed_pages_label.setText(failed_text)
#         self.failed_pages_label.setStyleSheet(
#             "font-weight: bold; color: red;" if "Failed Pages" in failed_text else
#             "font-weight: bold; color: green;"
#         )


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = StampCheckerApp()
#     window.show()
#     sys.exit(app.exec_())






import os
import sys
import re
import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader, PdfWriter

# Setup paths
if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

tesseract_path = os.path.join(base_path, 'tesseract_portable_windows', 'tesseract.exe')
pytesseract.pytesseract.tesseract_cmd = tesseract_path

poppler_path = os.path.join(base_path, 'Release-24.08.0-0', 'poppler-24.08.0', 'Library', 'bin')
pdf_path = os.path.join(base_path, 'TSI_POD_20191202.pdf')
sorted_pdf_path = os.path.join(base_path, 'Testing_pdf_sorted.pdf')


def extract_info(text):
    lines = text.splitlines()
    do_no = "UNKNOWN"

    # Step 1: Look for a line with "DO No." or similar and extract value
    for idx, line in enumerate(lines):
        if 'DO' in line and 'No' in line:
            match = re.search(r'\bDO\s*[\.\-:,]?\s*No[^A-Z0-9]*[:z]?\s*([A-Z0-9\-\/]{5,})', line, re.IGNORECASE)
            if match:
                do_no = match.group(1).strip()
                break
            else:
                # Look ahead a few lines for possible DO number
                for look_ahead in range(1, 3):
                    if idx + look_ahead < len(lines):
                        next_line = lines[idx + look_ahead].strip()
                        match_next = re.match(r'^(DO|MO|TST)[\-/\s]*[A-Z0-9\-\/]{5,}', next_line, re.IGNORECASE)
                        if match_next:
                            do_no = next_line
                            break
                if do_no != "UNKNOWN":
                    break

    # Step 2: Fallback – scan all lines for DO-/MO-/TST- patterns
    if do_no == "UNKNOWN":
        for line in lines:
            match = re.search(r'\b(DO|MO|TST)[\-/\s]*[A-Z0-9\-\/]{5,}', line.strip(), re.IGNORECASE)
            if match:
                do_no = match.group(0).strip()
                break

    # --- Company Extraction ---
    company = "UNKNOWN"
    for idx, line in enumerate(lines):
        if 'Ship To' in line:
            if idx + 1 < len(lines) and lines[idx + 1].strip():
                company = lines[idx + 1].split("Attention")[0].strip()
            elif idx + 2 < len(lines):
                company = lines[idx + 2].split("Attention")[0].strip()
            break

    return do_no, company

def extract_numbers(s):
    nums = re.findall(r'\d+', s)
    return [int(num) for num in nums] if nums else [-1]


# def ocr_text_from_image(image):
#     config = '--psm 6'
#     try:
#         full_text = pytesseract.image_to_string(image, config=config).strip()
#         return full_text.splitlines()  # return list of lines
#     except Exception as e:
#         return [f"OCR error: {e}"]


def ocr_text_from_image(image):
    psm_modes = [6, 3]  # Try in order of reliability
    for psm in psm_modes:
        config = f'--psm {psm}'
        try:
            text = pytesseract.image_to_string(image, config=config).strip()
            lines = text.splitlines()
            # If it finds potential DO number text, return early
            for line in lines:
                if 'DO' in line and 'No' in line:
                    return lines
        except Exception as e:
            continue
    # Fallback to last attempt
    return lines if 'lines' in locals() else [f"OCR error: Unable to extract text."]




def extract_page_no(text):
    # Try matching standard "Page No" formats first
    match = re.search(r'Page\s*(?:No\.?)?\s*(\d+)\s*(?:of\s*\d+)?', text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    
    # Fallback: look for lines like "3 of 8", "12 of 20", etc.
    fallback_match = re.search(r'\b(\d{1,3})\s+of\s+\d{1,3}\b', text)
    if fallback_match:
        return int(fallback_match.group(1))

    return None


def main(pdf_path):
    print(f"Reading PDF: {pdf_path}")
    images = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)

    page_data = []
    for i, pil_img in enumerate(images):
        cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
        lines = ocr_text_from_image(cv_img)
        text = "\n".join(lines)  # for use in extract_info & extract_page_no

        do_no, company = extract_info(text)
        page_no = extract_page_no(text)

        page_data.append({
            "index": i,
            "do_no": do_no,
            "company": company,
            "page_no": page_no,
            "text": text,
            "lines": lines
        })

    # Sort by company, then DO number, then page number
    sorted_pages = sorted(
    page_data,
    key=lambda x: (
        re.sub(r'\W+', '', x["company"].split()[0]).lower() if x["company"] else "",  # first word only
        x["do_no"],
        # x["page_no"] if x["page_no"] is not None else float('inf')
    )
)

    for page in sorted_pages:
        print(f"\n=== Page {page['index'] + 1}  ===")
        print(f"Company : {page['company']}")
        print(f"DO No   : {page['do_no']}")
        print(f"Page No : {page['page_no']}")
        # print(">> OCR Text Lines:")
        # for line in page['lines']:
        #     print(line)

    # Generate sorted PDF
    print(f"\nGenerating sorted PDF: {sorted_pdf_path}")
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    for page in sorted_pages:
        writer.add_page(reader.pages[page["index"]])

    with open(sorted_pdf_path, "wb") as f_out:
        writer.write(f_out)

    print("Sorted PDF generated successfully.")


if __name__ == "__main__":
    main(pdf_path)







# import sys
# import os
# import re
# import numpy as np
# import cv2
# from pdf2image import convert_from_path
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QPushButton, QLabel, QLineEdit,
#     QVBoxLayout, QHBoxLayout, QFileDialog, QTableWidget,
#     QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView,
#     QProgressBar
# )
# from PyQt5.QtCore import Qt, QThread, pyqtSignal
# from PyQt5.QtGui import QColor, QCursor
# from PyPDF2 import PdfReader, PdfWriter
# import pytesseract


# # Set poppler path
# if getattr(sys, 'frozen', False):
#     base_path = os.path.dirname(sys.executable)
# else:
#     base_path = os.path.dirname(os.path.abspath(__file__))

# poppler_path = os.path.join(base_path, 'Release-24.08.0-0', 'poppler-24.08.0', 'Library', 'bin')


# # Button styling function
# def style_button(button, color="#0078D4", hover_color="#005A9E", font_size=12):
#     button.setStyleSheet(f"""
#         QPushButton {{
#             background-color: {color};
#             color: white;
#             font-weight: bold;
#             font-size: {font_size}px;
#             border-radius: 6px;
#             padding: 6px 12px;
#         }}
#         QPushButton:hover {{
#             background-color: {hover_color};
#         }}
#         QPushButton:pressed {{
#             background-color: #004B87;
#         }}
#         QPushButton:disabled {{
#             background-color: gray;
#             color: white;
#         }}
#     """)
#     button.setCursor(QCursor(Qt.PointingHandCursor))


# class CheckWorker(QThread):
#     progress_update = pyqtSignal(int)
#     add_table_row = pyqtSignal(str, str, str, bool, bool, object, object)
#     update_summary = pyqtSignal(str, str)
#     done = pyqtSignal()
#     sorted_file_generated = pyqtSignal(str, str)  # filename, full path

#     def __init__(self, pdf_paths, poppler_path):
#         super().__init__()
#         self.pdf_paths = pdf_paths
#         self.poppler_path = poppler_path

#     def count_circles(self, img):
#         hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#         lower_blue = np.array([90, 50, 50])
#         upper_blue = np.array([130, 255, 255])
#         mask = cv2.inRange(hsv, lower_blue, upper_blue)
#         kernel = np.ones((3, 3), np.uint8)
#         mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#         mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
#         contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         count = 0
#         for cnt in contours:
#             area = cv2.contourArea(cnt)
#             if area < 300:
#                 continue
#             perimeter = cv2.arcLength(cnt, True)
#             approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
#             if len(approx) >= 8:
#                 count += 1
#         return count

#     # --- OCR and Sorting Helpers ---

#     def extract_numbers(self, s):
#         nums = re.findall(r'\d+', s)
#         return [int(num) for num in nums] if nums else [-1]

#     def extract_info(self, text):
#         do_no_match = re.search(r'DO\s*No\s*:\s*([^\s]+)', text, re.IGNORECASE)
#         do_no = do_no_match.group(1) if do_no_match else "UNKNOWN"

#         lines = text.splitlines()
#         company = "UNKNOWN"
#         for idx, line in enumerate(lines):
#             if 'Ship To' in line:
#                 if idx + 1 < len(lines):
#                     if lines[idx + 1].strip():
#                         company = lines[idx + 1].split("Attention")[0].strip()
#                     elif idx + 2 < len(lines):
#                         company = lines[idx + 2].split("Attention")[0].strip()
#                 break
#         return do_no, company

#     def ocr_text_from_image(self, image):
#         config = '--psm 6'
#         try:
#             return pytesseract.image_to_string(image, config=config).strip()
#         except Exception as e:
#             return f"OCR error: {e}"

#     def sort_pdf_pages(self, pdf_path, output_path):
#         # Convert PDF pages to images for OCR
#         try:
#             images = convert_from_path(pdf_path, dpi=300, poppler_path=self.poppler_path)
#         except Exception as e:
#             self.add_table_row.emit(f"Error loading PDF for sorting:", str(e), "", True, False, QColor("red"), None)
#             return False

#         page_data = []
#         for i, pil_img in enumerate(images):
#             cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
#             text = self.ocr_text_from_image(cv_img)
#             do_no, company = self.extract_info(text)
#             page_data.append({"index": i, "do_no": do_no, "company": company, "text": text})

#         sorted_pages = sorted(
#             page_data,
#             key=lambda x: (
#                 x["company"].strip().lower(),
#                 self.extract_numbers(x["do_no"].strip())
#             )
#         )

#         try:
#             reader = PdfReader(pdf_path)
#             writer = PdfWriter()
#             for page in sorted_pages:
#                 writer.add_page(reader.pages[page["index"]])
#             with open(output_path, "wb") as f_out:
#                 writer.write(f_out)
#             return True
#         except Exception as e:
#             self.add_table_row.emit(f"Error writing sorted PDF:", str(e), "", True, False, QColor("red"), None)
#             return False

#     def run(self):
#         total_files = len(self.pdf_paths)
#         total_pages = 0
#         total_pass = 0
#         total_fail = 0
#         overall_failed_pages = []

#         for path in self.pdf_paths:
#             if not os.path.isfile(path):
#                 continue

#             try:
#                 pages = convert_from_path(path, poppler_path=self.poppler_path)
#             except Exception as e:
#                 self.add_table_row.emit(f"Error loading PDF:", os.path.basename(path), str(e), True, False, QColor("red"), None)
#                 continue

#             self.add_table_row.emit(f"File: {os.path.basename(path)}", "", "", True, False, QColor("#000000"), QColor("#d9d9d9"))

#             file_pass = 0
#             file_fail = 0
#             file_failed_pages = []

#             for i, page in enumerate(pages):
#                 img = np.array(page)
#                 img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#                 lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#                 l, a, b = cv2.split(lab)
#                 clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
#                 cl = clahe.apply(l)
#                 enhanced_lab = cv2.merge((cl, a, b))
#                 img = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
#                 circle_count = self.count_circles(img)

#                 is_pass = circle_count >= 3
#                 result_text = "PASS" if is_pass else "FAIL"
#                 display_count = min(circle_count, 3)
#                 fg_color = QColor("green") if is_pass else QColor("red")

#                 self.add_table_row.emit(f"Page {i + 1}", str(display_count), result_text, False, False, fg_color, None)

#                 if is_pass:
#                     file_pass += 1
#                 else:
#                     file_fail += 1
#                     file_failed_pages.append(str(i + 1))

#             self.add_table_row.emit(
#                 f"Summary for {os.path.basename(path)}",
#                 f"Pages Passed: {file_pass}",
#                 f"Pages Failed: {file_fail}",
#                 True, True, QColor("blue"), QColor("#e1e1e1")
#             )

#             # Generate sorted PDF file
#             output_sorted_pdf = os.path.splitext(path)[0] + "_sorted.pdf"
#             success = self.sort_pdf_pages(path, output_sorted_pdf)
#             if success:
#                 self.add_table_row.emit(
#                     "Sorted PDF generated:",
#                     output_sorted_pdf,
#                     "",
#                     True, False, QColor("darkblue"), None
#                 )
#                 self.sorted_file_generated.emit(os.path.basename(output_sorted_pdf), output_sorted_pdf)
#             else:
#                 self.add_table_row.emit(
#                     "Sorted PDF generation failed.",
#                     "",
#                     "",
#                     True, False, QColor("red"), None
#                 )

#             self.add_table_row.emit("", "", "", False, False, None, QColor("#ffffff"))

#             total_pages += len(pages)
#             total_pass += file_pass
#             total_fail += file_fail
#             if file_fail > 0:
#                 overall_failed_pages.append(f"{os.path.basename(path)} (Pages: {', '.join(file_failed_pages)})")

#         overall_summary = (
#             f"Total Files: {total_files}    |    "
#             f"Total Pages: {total_pages}    |    "
#             f"Total Passed: {total_pass}    |    "
#             f"Total Failed: {total_fail}"
#         )
#         failed_text = "All pages passed successfully." if not overall_failed_pages else "Failed Pages:\n" + "\n".join(overall_failed_pages)

#         self.update_summary.emit(overall_summary, failed_text)
#         self.done.emit()


# class StampCheckerApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PDF Stamp Checker")
#         self.setGeometry(150, 100, 1000, 720)
#         self.pdf_paths = []
#         self.init_ui()

#     def init_ui(self):
#         layout = QVBoxLayout()

#         title_label = QLabel("PDF Stamp Checker")
#         title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
#         title_label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(title_label)

#         file_layout = QHBoxLayout()
#         self.file_entry = QLineEdit()
#         self.file_entry.setReadOnly(True)
#         self.file_entry.setMinimumHeight(30)
#         font = self.file_entry.font()
#         font.setPointSize(10)
#         self.file_entry.setFont(font)
#         file_layout.addWidget(self.file_entry)

#         browse_btn = QPushButton("Browse")
#         style_button(browse_btn)
#         browse_btn.setFixedWidth(100)
#         browse_btn.setToolTip("Select one or more PDF files to check")
#         browse_btn.clicked.connect(self.browse_files)
#         file_layout.addWidget(browse_btn)
#         layout.addLayout(file_layout)

#         self.start_btn = QPushButton("Start Checking")
#         self.start_btn.setEnabled(False)
#         self.start_btn.setFixedWidth(150)
#         style_button(self.start_btn, color="#06920D", hover_color="#04730B")
#         self.start_btn.setToolTip("Start checking selected files")
#         self.start_btn.clicked.connect(self.run_check)

#         btn_layout = QHBoxLayout()
#         btn_layout.addStretch()
#         btn_layout.addWidget(self.start_btn)
#         btn_layout.addStretch()
#         layout.addLayout(btn_layout)

#         self.file_label = QLabel("No file loaded")
#         self.file_label.setStyleSheet("font-style: italic; color: gray;")
#         layout.addWidget(self.file_label)

#         self.table = QTableWidget()
#         self.table.setColumnCount(3)
#         self.table.setHorizontalHeaderLabels(["Page", "Stamps Found", "Result"])
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
#         header = self.table.horizontalHeader()
#         font = header.font()
#         font.setBold(True)
#         header.setFont(font)
#         layout.addWidget(self.table)

#         self.progress_bar = QProgressBar()
#         self.progress_bar.setRange(0, 0)
#         self.progress_bar.setVisible(False)
#         layout.addWidget(self.progress_bar)

#         self.summary_label = QLabel("")
#         self.summary_label.setStyleSheet("font-weight: bold; color: navy;")
#         layout.addWidget(self.summary_label)

#         self.failed_pages_label = QLabel("")
#         self.failed_pages_label.setStyleSheet("font-weight: bold; color: red;")
#         layout.addWidget(self.failed_pages_label)

#         footer_label = QLabel("© 2025 MadebyCodeNest. All rights reserved.")
#         footer_label.setStyleSheet("color: gray; font-size: 10px;")
#         footer_label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(footer_label)

#         self.setLayout(layout)

#     def browse_files(self):
#         files, _ = QFileDialog.getOpenFileNames(self, "Select PDF files", "", "PDF Files (*.pdf)")
#         if files:
#             self.pdf_paths = files
#             display_text = ", ".join([os.path.basename(f) for f in files])
#             self.file_entry.setText(display_text)
#             self.file_label.setText(f"Loaded files: {display_text}")
#             self.file_label.setStyleSheet("color: black;")
#             self.start_btn.setEnabled(True)

#     def run_check(self):
#         if not self.pdf_paths:
#             QMessageBox.warning(self, "Error", "Please select at least one PDF file.")
#             return

#         self.table.setRowCount(0)
#         self.failed_pages_label.setText("")
#         self.summary_label.setText("")
#         self.start_btn.setEnabled(False)
#         self.progress_bar.setVisible(True)

#         self.worker = CheckWorker(self.pdf_paths, poppler_path)
#         self.worker.add_table_row.connect(self.insert_table_row)
#         self.worker.update_summary.connect(self.update_summary_labels)
#         self.worker.done.connect(self.on_check_finished)
#         self.worker.sorted_file_generated.connect(self.on_sorted_file_generated)
#         self.worker.start()

#     def on_check_finished(self):
#         self.progress_bar.setVisible(False)
#         self.start_btn.setEnabled(True)

#     def insert_table_row(self, col1, col2, col3, bold=False, italic=False, fg_color=None, bg_color=None):
#         row_idx = self.table.rowCount()
#         self.table.insertRow(row_idx)
#         item1 = QTableWidgetItem(col1)
#         item2 = QTableWidgetItem(col2)
#         item3 = QTableWidgetItem(col3)
#         font = item1.font()
#         font.setPointSize(10)
#         font.setBold(bold)
#         font.setItalic(italic)
#         for item in (item1, item2, item3):
#             item.setFont(font)
#             item.setForeground(fg_color or QColor(30, 30, 30))
#             if bg_color:
#                 item.setBackground(bg_color)
#         self.table.setItem(row_idx, 0, item1)
#         self.table.setItem(row_idx, 1, item2)
#         self.table.setItem(row_idx, 2, item3)

#     def update_summary_labels(self, summary_text, failed_text):
#         self.summary_label.setText(summary_text)
#         self.failed_pages_label.setText(failed_text)
#         self.failed_pages_label.setStyleSheet(
#             "font-weight: bold; color: red;" if "Failed Pages" in failed_text else
#             "font-weight: bold; color: green;"
#         )

#     def on_sorted_file_generated(self, filename, filepath):
#         QMessageBox.information(self, "Sorted PDF Generated", f"Sorted PDF saved as:\n{filepath}")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = StampCheckerApp()
#     window.show()
#     sys.exit(app.exec_())
