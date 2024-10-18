import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Accumulator')

        data = {
            0: ["7", "8", "9", "+", "("],
            1: ["4", "5", "6", "-", "）"],
            2: ["1", "2", "3", "*", "<-"],
            3: ["0", ".", "=", "/", "C"],
        }

        container = QVBoxLayout()

        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容")
        container.addWidget(edit)

        grid = QGridLayout()

        for line_number, line_data in data.items():
            for col_number, number in enumerate(line_data):
                # 此时col_number是第几列，number是要显示的符号
                btn = QPushButton(number)
                grid.addWidget(btn, line_number, col_number)

        container.addLayout(grid)

        self.setLayout(container)
        self.setWindowIcon(QIcon('Panda.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = myWindow()
    w.show()

    app.exec_()
