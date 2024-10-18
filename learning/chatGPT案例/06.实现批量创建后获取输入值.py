import time

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QComboBox, QSpinBox


class ExampleWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Dictionary to store controls
        self.controls = {}

        layout = QVBoxLayout(self)

        # Create a pair with QLineEdit
        line_edit_pair = self.createLabelControlPair("Line Edit:", QLineEdit(), None)
        layout.addLayout(line_edit_pair)

        # Create a pair with QComboBox
        combo_box_pair = self.createLabelControlPair("Combo Box:", QComboBox(), ["Item 1", "Item 2", "Item 3"])
        layout.addLayout(combo_box_pair)

        # Create a pair with QSpinBox
        spin_box_pair = self.createLabelControlPair("Spin Box:", QSpinBox(), range(1, 10))
        layout.addLayout(spin_box_pair)

        self.setLayout(layout)

    def createLabelControlPair(self, label_text, control, items):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        layout.addWidget(label)

        if isinstance(control, QComboBox):
            control.addItems(items)
        elif isinstance(control, QSpinBox):
            control.setRange(items.start, items.stop - 1)

        layout.addWidget(control)

        # Store the control in the dictionary with label_text as key
        self.controls[label_text] = control

        return layout

    def getControlData(self, label_text):
        control = self.controls.get(label_text)
        if isinstance(control, QLineEdit):
            return control.text()
        elif isinstance(control, QComboBox):
            return control.currentText()
        elif isinstance(control, QSpinBox):
            return control.value()
        return None


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = ExampleWidget()
    window.show()

    # Example usage of getControlData method
    print(window.getControlData("Line Edit:"))  # Will print the current text in the QLineEdit
    print(window.getControlData("Combo Box:"))  # Will print the selected item in the QComboBox
    print(window.getControlData("Spin Box:"))  # Will print the current value of the QSpinBox


    app.exec_()
    time.sleep(5)
    # Example usage of getControlData method
    print(window.getControlData("Line Edit:"))  # Will print the current text in the QLineEdit
    print(window.getControlData("Combo Box:"))  # Will print the selected item in the QComboBox
    print(window.getControlData("Spin Box:"))  # Will print the current value of the QSpinBox