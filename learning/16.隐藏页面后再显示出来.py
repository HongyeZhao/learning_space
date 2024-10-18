import time

from PyQt5.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("可隐藏和显示的窗口")
        self.setGeometry(300, 300, 200, 100)  # x, y, width, height

    def hide_window(self):
        self.hide()  # 隐藏窗口

    def show_window(self):
        self.show()  # 显示窗口

# 创建应用程序实例
app = QApplication([])
# 创建窗口实例
window = MyWindow()

# 显示窗口
window.show()

# 假设我们想要隐藏窗口
window.hide_window()

time.sleep(5)
# 如果我们稍后想要再次显示窗口1`
window.show_window()

# 运行应用程序
app.exec_()