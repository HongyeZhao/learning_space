import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QSpinBox, QComboBox, QGridLayout, QGroupBox
from PyQt5.QtCore import Qt

class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 主控件背景颜色
        main_bg_color = self.createColorPickerGroup('主控件背景颜色')
        layout.addWidget(main_bg_color)

        # 主控件边框颜色
        main_border_color = self.createColorPickerGroup('主控件边框颜色')
        layout.addWidget(main_border_color)

        # 控件控件/子控件背景颜色
        control_bg_color = self.createColorPickerGroup('控件控件/子控件背景颜色')
        layout.addWidget(control_bg_color)

        # 控件控件/子控件字体颜色
        control_text_color = self.createColorPickerGroup('控件控件/子控件字体颜色')
        layout.addWidget(control_text_color)

        # 主控件字体颜色
        main_text_color = self.createColorPickerGroup('主控件字体颜色')
        layout.addWidget(main_text_color)

        # 子控件字体颜色
        sub_text_color = self.createColorPickerGroup('子控件字体颜色')
        layout.addWidget(sub_text_color)

        # 主控件
        main_control_group = self.createControlGroup('主控件')
        layout.addWidget(main_control_group)

        # Slider 和 SpinBox 示例
        slider_spinbox_group = self.createSliderSpinBoxGroup()
        layout.addWidget(slider_spinbox_group)

        self.setLayout(layout)
        self.setWindowTitle('Color Picker Example')
        self.setGeometry(300, 300, 600, 400)

    def createColorPickerGroup(self, title):
        group_box = QGroupBox(title)
        layout = QGridLayout()

        for i in range(4):
            label = QLabel(f'R:')
            slider = QSlider(Qt.Horizontal)
            slider.setMaximum(255)
            spinbox = QSpinBox()
            spinbox.setMaximum(255)
            layout.addWidget(label, i, 0)
            layout.addWidget(slider, i, 1)
            layout.addWidget(spinbox, i, 2)

        group_box.setLayout(layout)
        return group_box

    def createControlGroup(self, title):
        group_box = QGroupBox(title)
        layout = QGridLayout()

        labels = ['文字字体:', '文字样式:', '文字大小:', '文字粗细:', '文字效果:']
        for i, text in enumerate(labels):
            label = QLabel(text)
            combo = QComboBox()
            combo.addItems(['选项1', '选项2', '选项3'])
            layout.addWidget(label, i, 0)
            layout.addWidget(combo, i, 1)

        group_box.setLayout(layout)
        return group_box

    def createSliderSpinBoxGroup(self):
        group_box = QGroupBox('Slider 和 SpinBox 示例')
        layout = QGridLayout()

        for i in range(2):
            slider = QSlider(Qt.Horizontal)
            slider.setMaximum(10)
            spinbox = QSpinBox()
            spinbox.setMaximum(10)
            layout.addWidget(slider, i, 0)
            layout.addWidget(spinbox, i, 1)

        group_box.setLayout(layout)
        return group_box

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColorPicker()
    ex.show()
    sys.exit(app.exec_())
