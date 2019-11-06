# to see how SelectDateTime dialog window and DigitalClock widget works

from PyQt5 import QtCore, QtGui, QtWidgets

from SelectDateTimeDialog import SelectDateTime
from DigitalClockWidget import DigitalClock

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 565)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_Store3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Store3.setGeometry(QtCore.QRect(60, 400, 321, 29))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Store3.setFont(font)
        self.pushButton_Store3.setObjectName("pushButton_Store3")

        self.pushButton_Store2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Store2.setGeometry(QtCore.QRect(580, 330, 331, 29))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Store2.setFont(font)
        self.pushButton_Store2.setObjectName("pushButton_Store2")

        self.pushButton_Store1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Store1.setGeometry(QtCore.QRect(60, 330, 321, 29))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Store1.setFont(font)
        self.pushButton_Store1.setObjectName("pushButton_Store1")

        self.pushButton_Store4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Store4.setGeometry(QtCore.QRect(580, 400, 331, 29))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Store4.setFont(font)
        self.pushButton_Store4.setObjectName("pushButton_Store4")

        self.pushButton_Reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Reset.setGeometry(QtCore.QRect(10, 60, 271, 29))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Reset.setFont(font)
        self.pushButton_Reset.setObjectName("pushButton_Reset")

        self.pushButton_SetDateTime = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SetDateTime.setGeometry(QtCore.QRect(10, 20, 271, 29))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SetDateTime.setFont(font)
        self.pushButton_SetDateTime.setObjectName("pushButton_SetDateTime")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(330, 20, 281, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout_SelectedDateTime = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_SelectedDateTime.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_SelectedDateTime.setObjectName("gridLayout_SelectedDateTime")

        self.label_SelectedDateTime = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_SelectedDateTime.setText("")
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_SelectedDateTime.setFont(font)
        self.label_SelectedDateTime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SelectedDateTime.setObjectName("label_SelectedDateTime")
        self.gridLayout_SelectedDateTime.addWidget(self.label_SelectedDateTime, 0, 0, 1, 1)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(580, 20, 380, 101))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_CurrentDateTime = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_CurrentDateTime.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_CurrentDateTime.setObjectName("gridLayout_CurrentDateTime")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Canteen System"))
        self.pushButton_Store3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_Store2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_Store1.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_Store4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_Reset.setText(_translate("MainWindow", "Reset to Current Date and Time"))
        self.pushButton_SetDateTime.setText(_translate("MainWindow", "Set Date and Time"))


# create a class to add connections and program logic for main window
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # to set up DigitalClockWidget
        self.DigitalClockWidget = DigitalClock()
        # add DigitalClock widget into prepared grid
        self.gridLayout_CurrentDateTime.addWidget(self.DigitalClockWidget, 0, 0, 0, 0)
        # when Set Date and Time button is clicked, open SelectDateTimeDialog
        self.pushButton_SetDateTime.clicked.connect(self.openSelectDateTimeDialog)
        # connect Reset to Current Date and Time
        self.pushButton_Reset.clicked.connect(self.ResetToCurrentDateAndTimeClicked)

    # create function to instantiate SelectDateTime dialog window and its class functions
    def openSelectDateTimeDialog(self):
        # instantiate SelectDateTime class
        self.SelectDateTimeDialog = SelectDateTime()
        # show SelectDateTime dialog window
        self.SelectDateTimeDialog.show()
        # connect Confirm button of SelectDateTime dialog window to ConfirmClicked function
        self.SelectDateTimeDialog.pushButton_Confirm.clicked.connect(self.ConfirmClicked)

    # When Reset Date and Time button is clicked, show Current Date and Time and hide Chosen Date and Time
    def ResetToCurrentDateAndTimeClicked(self):
        # hide grid containing label_SelectedDate time
        self.gridLayoutWidget.hide()
        # show grid containing DigitalClock widget
        self.gridLayoutWidget_2.show()

    # When Confirm button of SelectDateTime dialog window is clicked, update MainWindow
    # to display Chosen Date and Time, and hide Current Date and Time
    def ConfirmClicked(self):
        # Assign chosenDate with selected date from the calendarWidget
        chosenDate = self.SelectDateTimeDialog.userChosenDate()
        # Assign chosenDay with selected day from the calendarWidget (can be used to determine operating hours)
        chosenDay = self.SelectDateTimeDialog.getDayOfWeek()
        # Assign chosenTime with selected time from timeWidget
        chosenTime = self.SelectDateTimeDialog.userChosenTime()
        # set text of label to display chosen date and time
        # example: (aligned to center of grid)
        # Chosen Date and Time:
        # Wednesday, 6 November, 2019
        # 15:00
        self.label_SelectedDateTime.setText("Chosen Date and Time:\n" + chosenDate + "\n" + chosenTime)
        # show grid that display Chosen Date and Time (in the event that Reset to Current Date and Time button
        # is clicked first, and user decides to select preferred date and time and click on Set Date and Time button
        self.gridLayoutWidget.show()
        # hide grid that displays Current Date and Time
        self.gridLayoutWidget_2.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
