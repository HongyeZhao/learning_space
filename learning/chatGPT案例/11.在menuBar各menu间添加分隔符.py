import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Separator Example")
        self.setGeometry(100, 100, 600, 400)

        # 创建菜单栏
        menubar = self.menuBar()

        # 创建 "File" 菜单，并添加菜单项
        fileMenu = menubar.addMenu("File")
        fileMenu.addAction(QAction("New", self))
        fileMenu.addAction(QAction("Open", self))
        fileMenu.addAction(QAction("Exit", self))

        # 创建 "Edit" 菜单，并添加菜单项
        editMenu = menubar.addMenu("Edit")
        editMenu.addAction(QAction("Undo", self))
        editMenu.addAction(QAction("Redo", self))

        # 创建 "View" 菜单，并添加菜单项
        viewMenu = menubar.addMenu("View")
        viewMenu.addAction(QAction("Zoom In", self))
        viewMenu.addAction(QAction("Zoom Out", self))

        # 在菜单之间添加分隔符
        menubar.insertSeparator(1)  # 在 "File" 和 "Edit" 之间添加分隔符
        menubar.insertSeparator(2)  # 在 "Edit" 和 "View" 之间添加分隔符

        # 连接动作的信号到槽
        exitAction = QAction("Exit", self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

    def close(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())