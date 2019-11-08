from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

# create UI for SelectDateTime dialog (separate window)
class Ui_SelectDateTime(object):
    def setupUi(self, SelectDateTime,mainWindowController):
        self.mainWindowController=mainWindowController
        SelectDateTime.setObjectName("SelectDateTime")
        SelectDateTime.resize(616, 497)

        self.verticalLayout = QtWidgets.QVBoxLayout(SelectDateTime)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_titleDate = QtWidgets.QLabel(SelectDateTime)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_titleDate.setFont(font)
        self.label_titleDate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titleDate.setObjectName("label_titleDate")
        self.verticalLayout.addWidget(self.label_titleDate)

        self.calendarWidget = QtWidgets.QCalendarWidget(SelectDateTime)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Century Gothic\";\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(85, 170, 255);\n"
"border-color: rgb(170, 85, 0);\n"
"alternate-background-color: rgb(170, 255, 255);\n"
"background-color: rgb(238, 255, 246);")
        self.calendarWidget.setMinimumDate(
            QtCore.QDate(datetime.now().year, datetime.now().month, int(datetime.now().day)))
        self.calendarWidget.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)

        self.label_titleTime = QtWidgets.QLabel(SelectDateTime)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_titleTime.setFont(font)
        self.label_titleTime.setTextFormat(QtCore.Qt.RichText)
        self.label_titleTime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titleTime.setWordWrap(False)
        self.label_titleTime.setObjectName("label_titleTime")
        self.verticalLayout.addWidget(self.label_titleTime)

        self.timeEdit = QtWidgets.QTimeEdit(SelectDateTime)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit.setFont(font)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(datetime.now().year, datetime.now().month,
                                                                int(datetime.now().day)),
                                                   QtCore.QTime(datetime.now().hour, datetime.now().minute,
                                                                datetime.now().second)))
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 15, 10, 15)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Back = QtWidgets.QPushButton(SelectDateTime)
        self.pushButton_Back.setMaximumSize(QtCore.QSize(16777215, 50))
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
        self.pushButton_Back.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Back.setFont(font)
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.horizontalLayout.addWidget(self.pushButton_Back)
        self.pushButton_Confirm = QtWidgets.QPushButton(SelectDateTime)
        self.pushButton_Confirm.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Confirm.setFont(font)
        self.pushButton_Confirm.setObjectName("pushButton_Confirm")
        self.horizontalLayout.addWidget(self.pushButton_Confirm)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SelectDateTime)
        QtCore.QMetaObject.connectSlotsByName(SelectDateTime)

        # when Confirm button is clicked, return day chosen by the user (print date, followed by day)
        self.pushButton_Confirm.clicked.connect(self.comfirmClicked)
    def retranslateUi(self, SelectDateTime):
        _translate = QtCore.QCoreApplication.translate
        SelectDateTime.setWindowTitle(_translate("SelectDateTime", "Canteen System"))
        self.label_titleDate.setText(_translate("SelectDateTime", "Set Preferred Date"))
        self.label_titleTime.setText(_translate("SelectDateTime", "Set Preferred Time ( hh : mm )"))
        self.pushButton_Back.setText(_translate("SelectDateTime", "Back"))
        self.pushButton_Confirm.setText(_translate("SelectDateTime", "Confirm"))


class SelectDateTime(QtWidgets.QDialog, Ui_SelectDateTime):
    # initialise dialog window and connect functions with the buttons
    def __init__(self):
        super(SelectDateTime, self).__init__()
        self.setupUi(self)

        # when Confirm button is clicked, return day chosen by the user (print day of week, followed by date)
        self.pushButton_Confirm.clicked.connect(self.getDayOfWeek)
        # when Confirm button is clicked, return time chosen by the user

        # when Confirm button is clicked, close the dialog window
        self.pushButton_Confirm.clicked.connect(self.close)
        # when Back button is clicked, close the dialog window
        self.pushButton_Back.clicked.connect(self.close)

    # following functions are to return selected date and time on the
    # MainWindow UI and Stall Information UI where stall's information
    # will be printed according to the user's chosen date and time

    # this function is to return user chosen date from the calendarWidget widget
    def comfirmClicked(self):
        q_date=self.calendarWidget.selectedDate()
        q_time=self.timeEdit.time()
        q_dateTime=QtCore.QDateTime(q_date,q_time)
        self.mainWindowController.setSelectTime(q_dateTime.toPyDateTime())

    def userChosenDate(self):
        # obtain selected date from calendar widget and convert it to string
        self.date = self.calendarWidget.selectedDate().toString("dddd, dd MMMM, yyyy")
        print(self.date)  # for checking in terminal
        return self.date
        # example: returns 13/10/2019, Sunday

    # this function is to return user chosen time from the timeWidget
    def userChosenTime(self):
        # obtain selected time from timeEdit widget and convert it to string
        self.time = self.timeEdit.time().toString("HH:mm:ss")
        print(self.time)  # for checking in terminal
        return self.time
        # example: returns 12:00 if user selects 12:00

    # this function returns day of the week chosen by the user
    # day of the week is needed to determine the operating hours for the day
    def getDayOfWeek(self):
        # split the date string from userChosenDate into a list = ['dddd',' dd MMMM','yyyy']
        chosenDate = self.userChosenDate().split()
        # get string for day of the week --- 'dddd'
        chosenDay = chosenDate[0][:-1]
        print(chosenDay)
        return chosenDay
        # example: returns Sunday

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SelectDateTimeDialog = SelectDateTime()
    SelectDateTimeDialog.show()
    sys.exit(app.exec_())
