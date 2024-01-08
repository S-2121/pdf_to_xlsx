import sys

from PySide6.QtCore import Slot, QObject, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QQmlProperty

import main

class MainWindow(QQmlApplicationEngine):
    select_file_signal = Signal()
    def __init__(self):
        super().__init__()

        self.load("main.qml")
        self.rootContext().setContextProperty("MainWindow", self)
        self.window = self.rootObjects()[0]

        self.file_title_text = self.window.findChild(QObject, "file_title_text")
        self.file_title_name = QQmlProperty(self.file_title_text, "file_name")

        self.file_dialog = self.window.findChild(QObject, "file_dialog")
        self.file_dialog.selected_file_signal.connect(self.selected_file)

        self.convert_file_button = self.window.findChild(QObject, "convert_file_button")
        self.convert_file_button.convert_file_signal.connect(self.convert_file)

    @Slot()
    def selected_file(self, file_url):
        file_path = file_url.split("file:///")[1]
        # file_name = file_url.split("/")[-1]
        self.file_title_name.write(file_path)
    
    @Slot()
    def convert_file(self, file_path):
        main.load_file(file_path)

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
