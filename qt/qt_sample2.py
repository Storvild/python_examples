from PyQt5.QtWidgets import QApplication, QWidget
import sys, os


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.resize(250, 150)
        self.move(500, 300)
        self.setWindowTitle('Простой пример')
        self.show()
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWindow()
    sys.exit(app.exec_()) # "чистый" выход