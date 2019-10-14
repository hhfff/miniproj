from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow
import sys


if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui_MainWindow=Ui_MainWindow()
    ui_MainWindow.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
