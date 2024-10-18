import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenuBar, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_menubar()

    def initialize_menubar(self):
        # 创建菜单栏
        menu_bar = self.menuBar()

        # 创建 "文件" 菜单
        file_menu = menu_bar.addMenu("文件")

        # 创建 QAction 实例
        open_action = QAction("打开", self)
        open_action.setIcon(QIcon("open_icon.png"))  # 设置图标
        open_action.setShortcut("Ctrl+O")  # 设置快捷键
        open_action.setStatusTip("打开文件")  # 设置状态提示

        # 将 QAction 添加到菜单
        file_menu.addAction(open_action)

        # 连接信号和槽
        open_action.triggered.connect(self.on_open_action_triggered)

    def on_open_action_triggered(self):
        print("打开文件")

# 创建 QApplication 实例
app = QApplication(sys.argv)

# 创建主窗口
main_window = MainWindow()

# 显示主窗口
main_window.show()

# 运行应用程序
sys.exit(app.exec_())