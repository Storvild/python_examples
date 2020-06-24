from PyQt5.QtWidgets import QApplication, QWidget
import sys, os
from PyQt5 import QtChart

app = QApplication(sys.argv)

w = QWidget()
w.resize(250, 150)
w.move(500, 300)
w.setWindowTitle('Простой пример')

#print(help(QtChart))
chart = QtChart.QtChartView()


w.show()
        
sys.exit(app.exec_()) # "чистый" выход