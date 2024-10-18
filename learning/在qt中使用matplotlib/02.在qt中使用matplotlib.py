# 指定后端
import sys

import matplotlib as mpl
from PyQt5 import uic

mpl.use('Qt5Agg')

# 导入FigureCanvasQTAgg,实际上是一个Qt的控件，也可以像一般的控件一样添加到Qt的窗口中，相当于一个画布，用于存放图像（Figure）
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvas

# 导入Figure，就是图像本身，用于画图的各种操作
from matplotlib.figure import Figure



# import matplotlib.pyplot as plt
#
#
# fig = plt.figure(figsize=(3, 3), facecolor='lightskyblue',
#                  layout='constrained')
# fig.suptitle('A nice Matplotlib Figure')
# ax = fig.add_subplot()
# ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')
# plt.show()

from PyQt5.QtWidgets import *
from .FigureCanvas import MyFigure

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyFigure()
    ui = uic.loadUi("./neurosim.ui")
    ui.show()


