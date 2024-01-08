import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

import fitz
from openpyxl import Workbook

import convert
import edit

def load_file(file_path):
    try:
        dist_dir = "./dist/"

        pdf_doc = fitz.open(file_path)
        wb = Workbook()

        for page in pdf_doc:
            header_text_list = convert.conv_header(page)
            content_text_list = convert.conv_content(page)
            footer_text_list = convert.conv_footer(page)

            sheet_name = f"{header_text_list[0]}-{header_text_list[1]}"
            edit.init(wb, sheet_name)
            edit.edit_header(wb, sheet_name, header_text_list)
            edit.edit_content(wb, sheet_name, content_text_list)

        # Save the file
        # wb.remove(wb.get_sheet_by_name("Sheet"))
        wb.remove(wb["Sheet"])
        wb.save(dist_dir+"sample.xlsx")

        print("saved")
    except:
        print("error")

if __name__ == '__main__':
    load_file(sys.argv[1])