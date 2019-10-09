from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(591, 367)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 50, 361, 261))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setAutoFillBackground(True)
        self.calendarWidget.setMinimumDate(QtCore.QDate(currentYear, currentMonth, int(currentDay)))
        self.calendarWidget.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.titleDate = QtWidgets.QLabel(Dialog)
        self.titleDate.setGeometry(QtCore.QRect(90, 20, 201, 21))
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
        self.timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(410, 180, 151, 41))
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
        self.timeEdit.setObjectName("timeEdit")
        self.titleTime = QtWidgets.QLabel(Dialog)
        self.titleTime.setGeometry(QtCore.QRect(380, 150, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.titleTime.setFont(font)
        self.titleTime.setTextFormat(QtCore.Qt.RichText)
        self.titleTime.setWordWrap(False)
        self.titleTime.setObjectName("titleTime")
        self.pushButtonBack = QtWidgets.QPushButton(Dialog)
        self.pushButtonBack.setGeometry(QtCore.QRect(50, 320, 211, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 255, 149))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 255, 149))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 255, 149))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 255, 149))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonBack.setPalette(palette)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.pushButtonConfirm = QtWidgets.QPushButton(Dialog)
        self.pushButtonConfirm.setGeometry(QtCore.QRect(320, 320, 221, 41))
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Canteen System"))
        self.titleDate.setText(_translate("Dialog", "Set Preferred Date"))
        self.timeEdit.setDisplayFormat(_translate("Dialog", "hh:mm AP"))
        self.titleTime.setText(_translate("Dialog", "Set Preferred Time"))
        self.pushButtonBack.setText(_translate("Dialog", "Back"))
        self.pushButtonConfirm.setText(_translate("Dialog", "Confirm"))


class OpenSelectDateTimeDialog(QtWidgets.QDialog, Ui_Dialog, QtCore.QDate):
    global currentDay, currentMonth, currentYear, chosenDay, chosenMonth,chosenYear

    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year


    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        QtCore.QDate.__init__(self)
        self.setupUi(self)
        self.pushButtonBack.clicked.connect(self.hide)
        #print default date for cases where user does not change date
        print(self.calendarWidget.selectedDate().toString("dd-MM-yyyy"))
        self.calendarWidget.clicked.connect(self.userSelectedDate)

    #2 functions to return selected date and time on the
    #MainWindow UI / New Window UI where stall's information
    #will be printed according to the user chosen date and time
    def userSelectedDate(self):
        self.date = self.calendarWidget.selectedDate().toString("dd-MM-yyyy")
        print(self.date)
        return self.date

    #def userChosenTime(self):


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SelectDateTimeDialog = OpenSelectDateTimeDialog()
    SelectDateTimeDialog.show()
    sys.exit(app.exec_())


