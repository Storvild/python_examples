from PyQt5 import QtWidgets, uic
import sys, os

curdir = os.path.abspath(os.path.dirname(__file__))

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(os.path.join(curdir, 'qt_sample_ui.ui'), self) # Load the .ui file
        self.show() # Show the GUI
        
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application