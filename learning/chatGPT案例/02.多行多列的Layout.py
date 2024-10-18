import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QGroupBox, QLabel, QComboBox, QSpinBox, QVBoxLayout

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 创建主控件组
        main_control_group = QGroupBox('主控件')
        main_layout = QGridLayout()

        # 字体选项
        main_layout.addWidget(QLabel('文字字体:'), 0, 0)
        font_combo = QComboBox()
        font_combo.addItems(['宋体', '黑体', '楷体', '仿宋'])
        main_layout.addWidget(font_combo, 0, 1)

        # 文字样式
        main_layout.addWidget(QLabel('文字样式:'), 0, 2)
        style_combo = QComboBox()
        style_combo.addItems(['normal', 'italic', 'oblique'])
        main_layout.addWidget(style_combo, 0, 3)

        # 边框风格
        main_layout.addWidget(QLabel('边框风格:'), 0, 4)
        border_style_combo = QComboBox()
        border_style_combo.addItems(['none', 'solid', 'dashed', 'dotted'])
        main_layout.addWidget(border_style_combo, 0, 5)

        # 文字大小
        main_layout.addWidget(QLabel('文字大小:'), 1, 0)
        font_size_spinbox = QSpinBox()
        font_size_spinbox.setRange(1, 100)
        main_layout.addWidget(font_size_spinbox, 1, 1)

        # 文字粗细
        main_layout.addWidget(QLabel('文字粗细:'), 1, 2)
        weight_combo = QComboBox()
        weight_combo.addItems(['normal', 'bold'])
        main_layout.addWidget(weight_combo, 1, 3)

        # 边框大小
        main_layout.addWidget(QLabel('边框大小:'), 1, 4)
        border_size_spinbox = QSpinBox()
        border_size_spinbox.setRange(0, 10)
        main_layout.addWidget(border_size_spinbox, 1, 5)

        # 文字对齐
        main_layout.addWidget(QLabel('文字对齐:'), 2, 0)
        alignment_combo = QComboBox()
        alignment_combo.addItems(['左对齐', '居中', '右对齐'])
        main_layout.addWidget(alignment_combo, 2, 1)

        # 文字修饰
        main_layout.addWidget(QLabel('文字修饰:'), 2, 2)
        decoration_combo = QComboBox()
        decoration_combo.addItems(['none', 'underline', 'overline', 'line-through', 'blink'])
        main_layout.addWidget(decoration_combo, 2, 3)

        # 圆角大小
        main_layout.addWidget(QLabel('圆角大小:'), 2, 4)
        radius_spinbox = QSpinBox()
        radius_spinbox.setRange(0, 100)
        main_layout.addWidget(radius_spinbox, 2, 5)

        main_control_group.setLayout(main_layout)
        layout.addWidget(main_control_group)

        self.setLayout(layout)
        self.setWindowTitle('Custom Widget')
        self.setGeometry(300, 300, 600, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CustomWidget()
    ex.show()
    sys.exit(app.exec_())
