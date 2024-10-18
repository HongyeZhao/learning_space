from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialog Example")
        self.setGeometry(100, 100, 600, 400)

        # 创建一个按钮来打开文件选择框
        self.button = QPushButton("Open File Dialog", self)
        self.button.clicked.connect(self.openFileDialog)
        self.button.resize(self.button.sizeHint())
        self.button.move(250, 180)

    def openFileDialog(self):
        # 打开文件选择框
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # 可选，不使用系统默认对话框
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(f"Selected file: {fileName}")

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()