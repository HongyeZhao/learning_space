'''
画图
'''
# 指定后端
import sys

import matplotlib as mpl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

mpl.use('Qt5Agg')

# 导入FigureCanvasQTAgg,实际上是一个Qt的控件，也可以像一般的控件一样添加到Qt的窗口中，相当于一个画布，用于存放图像（Figure）
# 使用这个类时，需要传递一个图像对象
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvas

# 导入Figure，就是图像本身，用于画图的各种操作
from matplotlib.figure import Figure

class MyFigure(FigureCanvas):
    def __init__(self,parent=None):
        self.fig = Figure()
        super().__init__(self.fig)
        self.axes = self.fig.add_subplot(111)
        self.axes.clear()  # 清洗之前的图像
        self.axes.plot([1, 2, 3, 4],[2, 4, 6, 8])  # 画图
        self.fig.canvas.draw()  # 刷新画布


    # def plot(self, *args, **kwargs):
    #     self.axes.clear() # 清洗之前的图像
    #     self.axes.plot(*args, **kwargs) # 画图
    #     self.fig.canvas.draw()  # 刷新画布

# app = QApplication(sys.argv)
#
# w = QWidget()
# layout = QVBoxLayout(w)
# print(FigureCanvas)
# layout.addWidget(MyFigure)
# w.show()
#
# app.exec_()
