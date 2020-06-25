#!e:\virtualenvs\qt\qt_env36\Scripts\python.exe

import sys
from PyQt5.QtWidgets import QApplication, QWidget

print(sys.argv)

app = QApplication(sys.argv)
root = QWidget()
root.resize(640, 480)
root.setWindowTitle("Hello, World!")
root.show()
sys.exit(app.exec_())

