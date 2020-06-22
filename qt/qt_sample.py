from PyQt5.QtWidgets import QApplication, QWidget
import sys, os

app = QApplication(sys.argv)

w = QWidget()
w.resize(250, 150)
w.move(500, 300)
w.setWindowTitle('Простой пример')
w.show()
        
sys.exit(app.exec_()) # "чистый" выход