from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QToolBar, QAction

app = QApplication([])

window = QWidget()
window.setWindowTitle('Non-MainWindow Example')

# 创建菜单栏
menubar = QMenuBar(window)
window.setMenuBar(menubar)

# 创建一个菜单
fileMenu = menubar.addMenu('File')

# 创建一个动作
openAction = QAction('Open', window)
openAction.triggered.connect(lambda: print('Open action triggered'))

# 将动作添加到菜单中
fileMenu.addAction(openAction)

# 创建工具栏
toolBar = QToolBar('Tools')
window.addToolBar(toolBar)

# 将动作添加到工具栏中
toolBar.addAction(openAction)

window.show()
app.exec_()