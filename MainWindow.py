from PyQt5 import QtCore, QtGui, QtWidgets
from SelectDateTime import OpenSelectDateTimeDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 716)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setDateAndTimeButton = QtWidgets.QPushButton(self.centralwidget)
        self.setDateAndTimeButton.setGeometry(QtCore.QRect(10, 10, 181, 41))
        self.setDateAndTimeButton.setObjectName("setDateAndTimeButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Canteen System"))
        self.setDateAndTimeButton.setText(_translate("MainWindow", "Set Date and Time"))


class OpenMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setDateAndTimeButton.clicked.connect(self.SelectDateTimeDialog)

    def SelectDateTimeDialog(self):
        self.selectdatetimeWindow = QtWidgets.QDialog()
        self.SelectDateTimeUi = OpenSelectDateTimeDialog()
        self.SelectDateTimeUi.setupUi(self.selectdatetimeWindow)
        self.selectdatetimeWindow.show()
        self.SelectDateTimeUi.pushButtonBack.clicked.connect(self.SelectDateTimeUi.hide)
        self.selectdatetimeWindow.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = OpenMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
