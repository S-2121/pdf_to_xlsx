import sys

from PySide6.QtCore import Slot, QObject
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

class MainWindow(QQmlApplicationEngine):
    def __init__(self):
        super().__init__()
        self.load("main.qml")
        self.rootContext().setContextProperty("MainWindow", self)
        self.window = self.rootObjects()[0]

        self.select_file_button_area = self.window.findChild(QObject, "select_file_button_area")
        print(self.select_file_button_area)
        # self.select_file_button_area.select_file_signal.connect(self.select_file)

    @Slot()
    def select_file(self):
        print("here")

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
