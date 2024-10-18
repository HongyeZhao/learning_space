import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import scipy.io as sio

# from 在qt中使用matplotlib.FigureCanvas import MyFigure


class myUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("./neurosim.ui")
        plotWidget_tab1 = self.ui.plotWidget_tab1
        plotWidget_tab2 = self.ui.plotWidget_tab2
        plot_layout_tab1 = QVBoxLayout(plotWidget_tab1)
        plot_layout_tab2 = QVBoxLayout(plotWidget_tab2)
        fig_tab1 = Figure()
        fig_tab2 = Figure()
        canvas_tab1 = FigureCanvas(fig_tab1)
        canvas_tab2 = FigureCanvas(fig_tab2)
        plot_layout_tab1.addWidget(canvas_tab1)
        plot_layout_tab2.addWidget(canvas_tab2)
        ax_tab1 = fig_tab1.add_subplot(111)
        ax_tab2 = fig_tab2.add_subplot(111)
        ax_tab1.plot([1, 2, 3, 4],[1, 4, 9, 16])
        ax_tab2.plot([1, 2, 3, 4],[1, 4, 9, 16])

        mat_data = sio.loadmat('data_need_cluster_finalWC5000.mat')
        FCemp = mat_data['data_need_cluster']['FCemp']
        ax_tab1.imshow(FCemp[0][0], origin='lower')
        ax_tab2.imshow(FCemp[0][0], origin='lower')
        canvas_tab1.draw()
        canvas_tab2.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = myUI()
    w.ui.show()

    app.exec_()
