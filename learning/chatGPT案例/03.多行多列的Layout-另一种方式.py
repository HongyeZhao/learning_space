import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QGroupBox, QLabel, QComboBox, QSpinBox, QVBoxLayout, \
    QHBoxLayout

'''
    在一组控件外面再加一个layout布局容器
'''

class CustomWidget(QWidget):
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

        layout = QVBoxLayout()

        # 创建主控件组
        main_control_group = QGroupBox('主控件')
        main_layout = QGridLayout()

        # 添加每个标签和控件对到单独的水平布局中
        # 参数说明：控件、行、列、[行跨度、列跨度] 后两者代表控件应该跨越的行数和列数
        main_layout.addLayout(self.createLabelControlPair('文字字体:', QComboBox(), ['宋体', '黑体', '楷体', '仿宋']), 0, 0, 1, 2)
        main_layout.addLayout(self.createLabelControlPair('文字样式:', QComboBox(), ['normal', 'italic', 'oblique']), 0, 2,
                              1, 2)
        main_layout.addLayout(self.createLabelControlPair('边框风格:', QComboBox(), ['none', 'solid', 'dashed', 'dotted']),
                              0, 4, 1, 2)

        main_layout.addLayout(self.createLabelControlPair('文字大小:', QSpinBox(), range(1, 101)), 1, 0, 1, 2)
        main_layout.addLayout(self.createLabelControlPair('文字粗细:', QComboBox(), ['normal', 'bold']), 1, 2, 1, 2)
        main_layout.addLayout(self.createLabelControlPair('边框大小:', QSpinBox(), range(0, 11)), 1, 4, 1, 2)

        main_layout.addLayout(self.createLabelControlPair('文字对齐:', QComboBox(), ['左对齐', '居中', '右对齐']), 2, 0, 1, 2)
        main_layout.addLayout(self.createLabelControlPair('文字修饰:', QComboBox(),
                                                          ['none', 'underline', 'overline', 'line-through', 'blink']),
                              2, 2, 1, 2)
        main_layout.addLayout(self.createLabelControlPair('圆角大小:', QSpinBox(), [0, 101]), 2, 4, 1, 2)

        main_control_group.setLayout(main_layout)
        layout.addWidget(main_control_group)

        self.setLayout(layout) # 这很重要，所有创建的控件都需要在顶层Widget中显示，也就是本类的父对象QWidget
        self.setWindowTitle('Custom Widget')
        self.setGeometry(300, 300, 600, 200)

    def createLabelControlPair(self, label_text, control, items=None):  # items=None 设置默认参数避免未传参的情况
        layout = QHBoxLayout()
        label = QLabel(label_text)
        layout.addWidget(label)

        '''
        isinstance是Python的内建函数，由于检查一个对象是否是一个已知的类型，或则是否派生自那个类型。 \
        用法：isinstance(object, classinfo)
            object: 要检测的对象
            classinfo：一个类型或包含多个类型的元组
        若object是classinfo中某个类型的实例，isinstance就返回true，否则返回false
        '''
        if isinstance(control, QComboBox) and items:
            control.addItems(items)
        elif isinstance(control, QSpinBox):
            control.setRange(items[0], items[1] - 1)

        layout.addWidget(control)
        return layout


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CustomWidget()
    ex.show()
    sys.exit(app.exec_())
