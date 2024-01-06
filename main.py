# testtest

import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

import fitz
from openpyxl import Workbook

import convert
import edit

source_dir = "./source/"
dist_dir = "./dist/"


if __name__ == '__main__':
    # app = QGuiApplication(sys.argv)

    # engine = QQmlApplicationEngine()
    # engine.quit.connect(app.quit)
    # engine.load('main.qml')

    # sys.exit(app.exec())
    
    pdf_doc = fitz.open(source_dir+"sample.pdf")
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