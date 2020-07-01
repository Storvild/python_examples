from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
import sys, os
from PyQt5 import QtChart

app = QApplication(sys.argv)


w = QWidget()
w.resize(250, 150)
w.move(500, 300)
w.setWindowTitle('Простой пример')

layout = QVBoxLayout()
w.setLayout(layout)

chartview = QtChart.QChartView()
layout.addWidget(chartview)



w.show()
        
sys.exit(app.exec_()) # "чистый" выход