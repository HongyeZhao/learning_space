import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


# 新页面的类
class NewPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        label = QLabel("这是新页面")
        layout.addWidget(label)


# 当前页面的类
class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 创建按钮
        self.button = QPushButton("打开新页面")

        # 连接信号和槽
        self.button.clicked.connect(self.open_new_page)

        layout.addWidget(self.button)

    def open_new_page(self):
        # 关闭当前页面
        self.close()

        # 创建并显示新页面
        self.new_page = NewPage()
        self.new_page.show()


# 应用程序入口点
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_page = MainPage()
    main_page.show()
    sys.exit(app.exec_())