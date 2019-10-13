# Form implementation generated from reading ui file '.\SelectDateTime.ui'
# Created by: PyQt5 UI code generator 5.13.0

import sys

from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelectDateTime(object):
    def setupUi(self, SelectDateTime):
        SelectDateTime.setObjectName("SelectDateTime")
        SelectDateTime.resize(644, 413)
        SelectDateTime.setMaximumSize(QtCore.QSize(645, 413))

        self.calendarWidget = QtWidgets.QCalendarWidget(SelectDateTime)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 50, 361, 261))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setAutoFillBackground(True)
        self.calendarWidget.setMinimumDate(
            QtCore.QDate(datetime.now().year, datetime.now().month, int(datetime.now().day)))
        self.calendarWidget.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")

        self.titleDate = QtWidgets.QLabel(SelectDateTime)
        self.titleDate.setGeometry(QtCore.QRect(110, 20, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.titleDate.setFont(font)
        self.titleDate.setObjectName("titleDate")

        self.titleTime = QtWidgets.QLabel(SelectDateTime)
        self.titleTime.setGeometry(QtCore.QRect(420, 140, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.titleTime.setFont(font)
        self.titleTime.setTextFormat(QtCore.Qt.RichText)
        self.titleTime.setWordWrap(False)
        self.titleTime.setObjectName("titleTime")

        self.timeEdit = QtWidgets.QTimeEdit(SelectDateTime)
        self.timeEdit.setGeometry(QtCore.QRect(450, 180, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.timeEdit.setFont(font)
        self.timeEdit.setWrapping(True)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setCurrentSectionIndex(0)
        self.timeEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.timeEdit.setTime(QtCore.QTime(12, 0, 0))

        self.pushButtonBack = QtWidgets.QPushButton(SelectDateTime)
        self.pushButtonBack.setGeometry(QtCore.QRect(80, 360, 211, 41))
        self.pushButtonBack.setObjectName("pushButtonBack")

        self.pushButtonConfirm = QtWidgets.QPushButton(SelectDateTime)
        self.pushButtonConfirm.setGeometry(QtCore.QRect(380, 360, 221, 41))
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")

        self.retranslateUi(SelectDateTime)
        QtCore.QMetaObject.connectSlotsByName(SelectDateTime)

    def retranslateUi(self, SelectDateTime):
        _translate = QtCore.QCoreApplication.translate
        SelectDateTime.setWindowTitle(_translate("SelectDateTime", "Canteen System"))
        self.titleDate.setText(_translate("SelectDateTime", "Set Preferred Date"))
        self.titleTime.setText(_translate("SelectDateTime", "Set Preferred Time"))
        self.timeEdit.setDisplayFormat(_translate("SelectDateTime", "hh:mm AP"))
        self.pushButtonBack.setText(_translate("SelectDateTime", "Back"))
        self.pushButtonConfirm.setText(_translate("SelectDateTime", "Confirm"))

# create new class to open GUI generated from Qt Designer
class OpenSelectDateTimeWindow(QtWidgets.QWidget, Ui_SelectDateTime, QtCore.QDate):
    # initialise GUI and window
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        QtCore.QDate.__init__(self)
        self.setupUi(self)
        # when Back button is clicked, window is closed
        self.pushButtonBack.clicked.connect(self.close)
        # when Confirm button is clicked, return date chosen by the user
        self.pushButtonConfirm.clicked.connect(self.userChosenDate)
        # when Confirm button is clicked, return time chosen by the user
        self.pushButtonConfirm.clicked.connect(self.userChosenTime)

    # 2 functions to return selected date and time on the
    # MainWindow UI / New Window UI where stall's information
    # will be printed according to the user chosen date and time

    # this function is to return user chosen date from the calendarWidget widget
    def userChosenDate(self):
        self.date = self.calendarWidget.selectedDate().toString("dd-MM-yyyy, dddd")
        print(self.date)  # for checking in terminal
        return self.date
        #example: returns 13-10-2019, Sunday

    # this function is to return user chosen time from the timeEdit widget
    def userChosenTime(self):
        self.time = self.timeEdit.time().toString("HH:mm")
        print(self.time)  # for checking in terminal
        return self.time
        #example: returns 12:00 if user selects 12:00 PM
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    SelectDateTimeWindow = OpenSelectDateTimeWindow()
    SelectDateTimeWindow.show()
    sys.exit(app.exec_())
    
