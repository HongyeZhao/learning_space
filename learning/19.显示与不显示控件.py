from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        self.button = QPushButton("隐藏按钮")
        self.hide_button = QPushButton("点击隐藏上面的按钮")

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.hide_button)

        self.hide_button.clicked.connect(self.button.setVisible, False)

        self.setWindowTitle("控件隐藏示例")
        self.resize(200, 100)

if __name__ == '__main__':
    app = QApplication([])
    example = Example()
    example.show()
    app.exec_()