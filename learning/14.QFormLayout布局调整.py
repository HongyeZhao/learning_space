import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QPushButton, QLabel

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 创建表单布局
        form_layout = QFormLayout()
        self.setLayout(form_layout)

        # 创建用户名和密码的标签与输入框
        username_label = QLabel("用户名:")
        username_edit = QLineEdit()
        password_label = QLabel("密码:")
        password_edit = QLineEdit()
        password_edit.setEchoMode(QLineEdit.Password)  # 密码输入框

        # 添加到表单布局，并设置样式表
        form_layout.addRow(username_label, username_edit)
        form_layout.addRow(password_label, password_edit)

        # 设置输入框的样式表
        username_edit.setStyleSheet("QLineEdit { width: 20px; }")
        password_edit.setStyleSheet("QLineEdit { width: 20px; }")

        # 创建登录按钮
        login_button = QPushButton("连接")
        form_layout.addRow(login_button)

        # 设置窗口标题和初始大小
        self.setWindowTitle("用户登录界面")
        self.resize(250, 150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())