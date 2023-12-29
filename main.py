# import sys

# from PySide6.QtGui import QGuiApplication
# from PySide6.QtQml import QQmlApplicationEngine

import fitz
import convert

source_dir = "./source/"
dist_dir = "./dist/"

# app = QGuiApplication(sys.argv)

# engine = QQmlApplicationEngine()
# engine.quit.connect(app.quit)
# engine.load('main.qml')

# sys.exit(app.exec())

# import tabula
# dfs = tabula.read_pdf(source_dir+"sample.pdf", pages="all")
# len(dfs)

if __name__ == '__main__':
    doc = fitz.open(source_dir+"sample.pdf") 
    
    page = doc[0]
    
    
    header_text_list = convert.conv_header(page)
    content_text_list = convert.conv_content(page)
    footer_text_list = convert.conv_footer(page)