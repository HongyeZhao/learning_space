import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QApplication, QVBoxLayout


class myWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 300)
        self.setWindowTitle("QHBoxLayout")

        layout = QVBoxLayout()


        button1 = QPushButton("按钮1")
        layout.addWidget(button1)


        button2 = QPushButton("按钮2")
        layout.addWidget(button2)


        button3 = QPushButton("按钮3")
        layout.addWidget(button3)


        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWindow()
    w.show()
    app.exec_()