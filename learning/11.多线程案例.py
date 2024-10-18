import json
import sys
import time

import requests
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication


class MyThread(QThread):

    start_login_signal = pyqtSignal(str)

    #  signal传递过来了UI线程中的自定义信号
    def __init__(self, signal):
        super().__init__()
        self.login_complete_signal = signal

    def login_by_requests(self, user_password_json):
        # 将json字符串转换为字典，从而实现传递用户名以及密码
        user_password_dict = json.loads(user_password_json)
        print(user_password_dict.get("user_name"))
        print(user_password_dict.get("password"))

        # 使用requests模块发送请求（POST）
        # 但是腾讯云下架了云函数中的API服务，无法用
        # r = requests.post(url="xxxxxx",json=user_password_json)
        # print("接受到腾讯服务器响应：", r.content.decode())
        # ret = r.json()

        # 发送信号给UI线程
        self.login_complete_signal.emit(user_password_json)


    def run(self):
        while True:
            print("thread is running")
            time.sleep(1)




class MyWindow(QWidget):

    login_status_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./myWindow.ui")
        self.login_btn = self.ui.pushButton_2
        self.forget_pwd_btn = self.ui.pushButton
        self.username = self.ui.LineEdit
        self.password = self.ui.LineEdit_2
        self.textBrower = self.ui.textEdit

        # create thread and run it
        self.login_thread = MyThread(self.login_status_signal)
        self.login_thread.start()

        # 绑定自定义信号
        self.login_thread.start_login_signal.connect(self.login_thread.login_by_requests)
        self.login_status_signal.connect(self.login_status)
        # 绑定点击信号
        self.login_btn.clicked.connect(self.login)

    def login(self):
        """登录按钮的槽函数"""
        user_name = self.username.text()
        password = self.password.text()
        self.login_thread.start_login_signal.emit(json.dumps({"user_name": user_name, "password": password}))

    def login_status(self, status):
        print("status.....", status)
        status_dict = json.loads(status)
        self.textBrower.setText(f"用户：{status_dict.get('user_name')} 登录成功")
        self.textBrower.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.ui.show()

    app.exec_()