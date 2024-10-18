import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styled QTextEdit Example")
        self.setGeometry(100, 100, 800, 600)

        # 创建 QTextEdit 控件
        self.textEdit = QTextEdit()
        self.textEdit.setPlainText("Hello, this is some initial text.")
        self.textEdit.append("QTextEdit supports rich text formatting.")

        # 设置字体
        font = QFont("Arial", 12)  # 你可以选择任何你喜欢的字体和大小
        self.textEdit.setFont(font)

        # 使用样式表来定制 QTextEdit 的外观
        self.textEdit.setStyleSheet("""
            QTextEdit {
                background-color: #FFFFFF;  /* 背景色 */
                border: 2px solid #CCCCCC;  /* 边框 */
                border-radius: 10px;  /* 边框圆角 */
                padding: 5px;  /* 内边距 */
            }
            QTextEdit:focus {
                border: 2px solid #4A90DA;  /* 聚焦时的边框颜色 */
            }
        """)

        # 创建中心窗口部件和布局
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        # 将 QTextEdit 添加到布局中
        layout.addWidget(self.textEdit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())