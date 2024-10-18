import sys

from PyQt5.QtWidgets import *


class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel("this is words")
        label.setStyleSheet("font-size:30px;color:red;")

        menu = self.menuBar()
        menu.setNativeMenuBar(False)

        file_menu = menu.addMenu("文件")
        file_menu.addAction("新建")
        file_menu.addAction("保存")

        edit_menu = menu.addMenu("编辑")
        edit_menu.addAction("编辑")
        edit_menu.addAction("paste")
        edit_menu.addAction("cut")

        self.setCentralWidget(label)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = myWindow()

    w.show()

    app.exec()
