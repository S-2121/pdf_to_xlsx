# chsong_240106

import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

import fitz
from openpyxl import Workbook

import convert
import edit

def load_file(parent = None, file_path = "./"):
    try:
        if parent:
            parent.convert_file_button_text.write("변환중...")
        else:
            print("converting...")

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
        ws_name_list = wb.sheetnames
        if "Sheet" in ws_name_list:
            wb.remove(wb["Sheet"])
        wb.save(dist_dir+"sample.xlsx")

        if parent:
            parent.convert_file_button_text.write("변환 완료")
        else:
            print("saved")
    except:
        if parent:
            parent.convert_file_button_text.write("변환 실패")
        else:
            print("error")

if __name__ == '__main__':
    load_file(None, sys.argv[1])