import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Open Folder Example')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.button = QPushButton('Open Folder')
        self.button.clicked.connect(self.open_folder)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def open_folder(self):
        # # 打开文件夹对话框，设置起始路径为用户的主目录
        # folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "/home")
        # if folder_path:
        #     print(f"Selected Folder: {folder_path}")
        # os.startfile("D:\\库\\文档\\WeChat Files\\wxid_hm01f8nbif2222\\FileStorage\\File\\2024-09\\")
        cwd = os.getcwd()
        print(cwd)
        data_path = os.path.join(cwd, "..", "..", "test")
        print(data_path)
        os.startfile(cwd)
        os.startfile(data_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())
