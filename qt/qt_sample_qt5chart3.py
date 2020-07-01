from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5 import QtChart
from PyQt5.QtGui import QPainter
import sys, os

app = QApplication(sys.argv)


w = QWidget()
w.resize(250, 150)
w.move(500, 300)
w.setWindowTitle('Круговая диаграмма')
w.setGeometry(100,100, 680,500)

layout = QVBoxLayout()
w.setLayout(layout)

series = QtChart.QPieSeries()
series.append("Jane", 1);
series.append("Joe", 2);
series.append("Andy", 3);
series.append("Barbara", 4);
series.append("Axel", 5);

chart = QtChart.QChart()
chart.addSeries(series)
chart.setTitle('Простой пример круговой диаграммы')

chartview = QtChart.QChartView(chart)
chartview.setRenderHint(QPainter.Antialiasing)
layout.addWidget(chartview)


w.show()
        
sys.exit(app.exec_()) # "чистый" выход