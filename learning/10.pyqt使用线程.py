import sys
import time

from PyQt5 import uic
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QApplication


class myThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(5):
            time.sleep(1)
            print(f"lallala {i}")


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./myWindow.ui")

        login = self.ui.pushButton_2
        login.clicked.connect(self.clicked1)

    def clicked1(self):
        self.my_thread = myThread()
        self.my_thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.ui.show()

    app.exec_()
