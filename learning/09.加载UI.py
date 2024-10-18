"""
动态加载ui文件
"""

import sys
import time

import self as self
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./myWindow.ui")
        self.username = self.ui.LineEdit
        self.password = self.ui.LineEdit_2
        self.login_btn = self.ui.pushButton_2
        self.forgetpwd_btn = self.ui.pushButton
        self.text_browser = self.ui.textEdit

        self.login_btn.clicked.connect(self.login)

    def login(self):
        """"实现登录逻辑"""
        print("login.....")
        user_name = self.username.text()
        pwd = self.password.text()

        for i in range(1,5):
            time.sleep(1)
            print(i)

        if user_name == 'admin' and pwd == '123':
            self.text_browser.setText("欢迎%s" %user_name)
            self.text_browser.repaint()
        else:
            self.text_browser.setText("用户名或密码错误...请重试")
            self.text_browser.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.ui.show()


    app.exec_()
