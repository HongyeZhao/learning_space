import sys
from PyQt5.QtWidgets import *
class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 最外层布局器
        container = QVBoxLayout()

        # 第一组
        # 爱好容器（v_layout）保证控件垂直分布
        hobby_v_layout = QVBoxLayout()
        # hobby_box 不是必要的，主要是保证三个控件是一个组的，和下面区分开，美观
        hobby_box = QGroupBox("Hobby")
        btn1 = QRadioButton("smoking")
        btn2 = QRadioButton("drinking")
        btn3 = QRadioButton("hotHair")
        # 将三个控件追加到爱好容器中
        hobby_v_layout.addWidget(btn1)
        hobby_v_layout.addWidget(btn2)
        hobby_v_layout.addWidget(btn3)
        # 在hobby_box中添加布局
        hobby_box.setLayout(hobby_v_layout)

        # 第二组
        gender_h_layout = QHBoxLayout()
        gender_box = QGroupBox("Gender")
        btn4 = QRadioButton('man')
        btn5 = QRadioButton('male')
        gender_h_layout.addWidget(btn4)
        gender_h_layout.addWidget(btn5)
        gender_box.setLayout(gender_h_layout)

        container.addWidget(hobby_box)
        container.addWidget(gender_box)
        self.setLayout(container)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWindow()
    w.show();
    app.exec_()