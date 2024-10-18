from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QVBoxLayout

# 创建 QApplication 实例
app = QApplication([])

# 创建 QMainWindow 实例
main_window = QMainWindow()

# 创建 QTabWidget 实例
tab_widget = QTabWidget()


# 创建第一个选项卡
tab1 = QWidget()
tab1_layout = QVBoxLayout()  # 创建一个垂直布局
label1 = QLabel("这是第一个选项卡的内容")
tab1_layout.addWidget(label1)
tab1.setLayout(tab1_layout)

# 创建第二个选项卡
tab2 = QWidget()
tab2_layout = QVBoxLayout()  # 创建另一个垂直布局
label2 = QLabel("这是第二个选项卡的内容")
tab2_layout.addWidget(label2)
tab2.setLayout(tab2_layout)

# 将选项卡添加到 QTabWidget
tab_widget.addTab(tab1, "选项卡 1")
tab_widget.addTab(tab2, "选项卡 2")

# 将 QTabWidget 设置为主窗口的中央部件
main_window.setCentralWidget(tab_widget)

# 显示主窗口
main_window.show()

# 启动应用程序的事件循环
app.exec_()