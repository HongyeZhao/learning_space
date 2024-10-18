import sys

from PyQt5.QtWidgets import *


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("I am the first stack",self)
        self.setStyleSheet("background-color:blue;")


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("I am the second stack",self)
        self.setStyleSheet("background-color:red;")


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.create_stacked_layout()
        self.init_ui()

    def create_stacked_layout(self):
        # 若不加self，stacked_layout就是局部变量，在函数外面用不了
        self.stacked_layout = QStackedLayout()
        # 创建单独的widget
        win1 = Window1()
        win2 = Window2()
        # 将创建的2个Widget添加到抽屉布局器中
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):
        # 设置widget大小以及固定的宽高
        self.setFixedSize(300, 270)

        # 整体的布局容器
        container = QVBoxLayout()

        # 存放抽屉的子widget
        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet("background-color:grey")

        # 用来切换抽屉的按钮
        btn1 = QPushButton("stack1")
        btn2 = QPushButton("stack2")
        # 为按钮添加事件
        btn1.clicked.connect(self.btn1_clicked)
        btn2.clicked.connect(self.btn2_clicked)

        # 将需要显示的控件加入到布局容器中
        container.addWidget(widget)
        container.addWidget(btn1)
        container.addWidget(btn2)

        self.setLayout(container)

    # 点击时间处理函数
    def btn1_clicked(self):
        self.stacked_layout.setCurrentIndex(0)

    def btn2_clicked(self):
        self.stacked_layout.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MyWindow()
    win.show()

    app.exec_()
