import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QComboBox, QSpinBox, QVBoxLayout, QHBoxLayout, QWidget, QLabel, \
    QGroupBox, QTextEdit


class params(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
                QGroupBox {
                    border: 1px solid gray;
                    border-radius: 5px;
                    margin-top: 1ex;
                    font-weight: bold;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    subcontrol-position: top left;
                    padding: 0 3px;
                }
                QLabel {
                    font-size: 14px;
                }
                QComboBox, QSpinBox {
                    min-width: 80px;
                }
                """)

        # 最外层布局
        layout = QVBoxLayout()

        main_contral_group = QGroupBox("主控件")
        # 组内的栅格布局
        main_layout = QGridLayout()

        main_layout.addLayout(self.createLabelControlPair("文字字体:", QComboBox(), ['宋体', '黑体', '楷体', '仿宋']), 0, 0, 1, 2)
        main_layout.addLayout(self.createLabelControlPair("文字样式:", QComboBox(), ['normal', '瘦金体', '赵体']), 0, 2, 1, 2)
        main_layout.addLayout(self.createLabelControlPair("边框风格:", QComboBox(), ['none', '瘦金体', '赵体']), 0, 4, 1, 2)
        main_layout.addLayout(self.createLabelControlPair("文字大小:", QSpinBox(), range(1, 31)), 1, 0, 1, 2)
        main_layout.addLayout(self.createLabelControlPair("文字粗细:", QComboBox(), ['normal', '瘦金体', '赵体']), 1, 2, 1, 2)
        main_layout.addLayout(self.createLabelControlPair("边框大小:", QSpinBox(), range(1,31)), 1, 4, 1, 2)
        main_layout.addLayout(self.createLabelControlPair("文字对齐:", QComboBox(), ['左对齐', '瘦金体', '赵体']), 2, 0, 1, 2)
        main_layout.addLayout(self.createLabelControlPair("文字修饰:", QComboBox(), ['none', '瘦金体', '赵体']), 2, 2, 1, 2)
        main_layout.addLayout(self.createLabelControlPair("圆角大小:", QSpinBox(), range(1, 31)), 2, 4, 1, 2)

        main_contral_group.setLayout(main_layout)


        # 在下面添加一个输出框
        main_text_edit = QTextEdit()
        main_text_edit.setPlaceholderText("等待输出结果")


        layout.addWidget(main_contral_group)
        layout.addWidget(main_text_edit)
        self.setLayout(layout)
        self.setWindowTitle("Custom Widget")
        self.setGeometry(300, 300, 600, 200)




    def createLabelControlPair(self, label_text, control, items):
        layout = QHBoxLayout()
        lable = QLabel(label_text)
        layout.addWidget(lable)

        if isinstance(control, QComboBox):
            control.addItems(items)
        elif isinstance(control, QSpinBox):
            control.setRange(items.start, items.stop - 1)

        layout.addWidget(control)
        return layout



if __name__ == '__main__':
    app = QApplication(sys.argv)

    params = params()
    params.show()


    sys.exit(app.exec_())
