import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

from 在qt中使用matplotlib.FigureCanvas import MyFigure


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("./neurosim.ui")

    ui.show()

    app.exec_()