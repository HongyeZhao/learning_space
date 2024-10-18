import sys

from PyQt5 import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QDesktopWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget();

    w.setWindowTitle("第一个PyQt")

    # lable = QLabel("账号：")
    lable = QLabel("账号：", w)
    lable.setGeometry(20, 20, 30, 20)
    lable.setParent(w)

    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(55, 20, 200, 20)

    w.resize(1000,800)

    w.move(0, 0)
    center_pointer = QDesktopWidget().availableGeometry().center()
    print(center_pointer)
    new_x = center_pointer.x()
    new_y = center_pointer.y()
    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    old_x, old_y, weight, hight = w.frameGeometry().getRect()
    w.move((int)(new_x - weight/2), (int)(new_y - hight/2))
    w.setWindowIcon(QIcon('Panda.png'))
    w.setWindowFlags(Qt.Qt.CustomizeWindowHint)
    w.show()

    app.exec_()