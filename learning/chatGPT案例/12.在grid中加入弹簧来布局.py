import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QSpacerItem, QSizePolicy

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout with Spacers")
        self.setGeometry(100, 100, 300, 200)

        # 创建一个按钮
        button = QPushButton("Press Me", self)

        # 创建网格布局
        grid_layout = QGridLayout(self)

        # 添加按钮到第一行第一列
        grid_layout.addWidget(button, 0, 0)

        # 创建水平弹簧（占位符）
        horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # 创建垂直弹簧（占位符）
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # 添加水平弹簧到第一行的最后一列
        grid_layout.addItem(horizontal_spacer, 0, 1)

        # 添加垂直弹簧到第二列
        grid_layout.addItem(vertical_spacer, 1, 0)

        # 使布局生效
        self.setLayout(grid_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())