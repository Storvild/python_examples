#from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui, QtWidgets
#import PyQt5.QtGui
import sys, os

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 640, 480)
        #x = numpy.linspace(0, 2.0*numpy.pi, 101)
        #y = numpy.sin(x)
        #plt.plot(x, y)
        
        label = QtWidgets.QLabel('Hello', self)
        
        layout = QtWidgets.QVBoxLayout() #было self
        layout.addWidget(label)
        
        #qwidget = QtWidgets.QWidget
        #layout.addWidget(qwidget)
        
        fig = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvasQTAgg(fig)
        canvas.axes = fig.add_subplot(111)
        canvas.axes.grid()
        canvas.setParent(self)
        
        
        #layout.addWidget(canvas)
        #canvas.show()
        
        
        #fig, ax = plt.subplots()
        #ax.plot([1, 2], [2, 3]) 
        #ax.grid()
        #canvas = FigureCanvasQTAgg(fig)
        #layout.addWidget(canvas)
        #canvas.draw()
        
        #self.canvas = FigureCanvasQTAgg(fig)
    
        #self.figure = Figure()
        #self.canvas = FigureCanvasQTAgg(fig) 
        #self.canvas = FigureCanvasQTAgg(self.figure) # Было (self.fi)
        #self.canvas = FigureCanvasQTAgg(fig)
        
        #self.addWidget(self.canvas)
        self.toolbar = NavigationToolbar2QT(canvas, self)
        self.show()
        
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    m = MainWindow()
    sys.exit(app.exec_()) # "чистый" выход