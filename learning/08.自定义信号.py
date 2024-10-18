import sys
import time

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import *

class MyWindow(QWidget):

    mySignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()

    def init_ui(self):
        self.resize(300, 200)

        container = QVBoxLayout()

        self.msg = QLabel("")
        self.msg.resize(440, 15)
        self.msg.setWordWrap(True) #自动换行
        self.msg.setAlignment(Qt.AlignTop)

        # 创建一个滚动对象
        scroll = QScrollArea()
        scroll.setWidget(self.msg)

        # 创建垂直布局容器，用来添加自动滚动条
        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        # 创建水平布局容器
        h_layout = QHBoxLayout()
        btn = QPushButton("开始检测", self)
        h_layout.addStretch(1)
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        btn.clicked.connect(self.check)
        self.mySignal.connect(self.mySlot)

        # 操作将要显示的控件以及子布局容器添加到container
        container.addLayout(v_layout)
        container.addLayout(h_layout)
        self.setLayout(container)

    def mySlot(self, msg):
        print(msg)
        self.msg_history.append(msg)
        self.msg.setText("<br>".join(self.msg_history))
        self.msg.resize(440, self.msg.frameSize().height() + 15)
        self.msg.repaint()

    def check(self):
        for i, ip in enumerate(["192.168.1.%d" % x for x in range(1, 255)]):
            msg = "模拟，正在检测 %s 上的漏洞..." % ip
            print(msg)
            if i % 5 == 0:
                self.mySignal.emit(msg + "[there is a bug]")
            time.sleep(0.01)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()

