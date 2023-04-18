from JTODAPP.JtoDapp import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import JTODAPP.jtod
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()