from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow
import sys
app = QApplication(sys.argv)
myWidget = QWidget()
myWidget.show()
myMainWindow = QMainWindow()

menu = myMainWindow.menuBar()

model_menu = menu.addMenu("模型")
analyze_menu = menu.addMenu("分析方法")
deeplearning_menu = menu.addMenu("DeepLearning")

model_menu.addAction("WC66_Model")
model_menu.addAction("dmf_Model")
analyze_menu.addAction("cps")
analyze_menu.addSeparator()
analyze_menu.addAction("lda")
analyze_menu.addAction("svm")
analyze_menu.addAction("bct")
analyze_menu.addAction("cps")
deeplearning_menu.addAction("eeg1")
deeplearning_menu.addAction("eeg2")
deeplearning_menu.addAction("eeg3")



myMainWindow.show()
sys.exit(app.exec_())
