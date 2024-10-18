from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

app = QApplication([])

# 创建窗口和布局
window = QWidget()
gridLayout = QGridLayout(window)

# 创建按钮
button = QPushButton("Centered Button")

# 添加空列和按钮
gridLayout.setColumnStretch(0, 1)  # 左侧空列，伸展系数为1
gridLayout.addWidget(button, 1, 1)  # 在第二行、第二列添加按钮
gridLayout.setColumnStretch(2, 1)  # 右侧空列，伸展系数为1

# 添加空行，以确保按钮上下也居中
gridLayout.setRowStretch(0, 1)  # 上面空行，伸展系数为1
gridLayout.setRowStretch(2, 1)  # 下面空行，伸展系数为1

# 设置布局并显示窗口
window.setLayout(gridLayout)
window.show()

app.exec_()
