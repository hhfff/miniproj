from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

# designed by Stanley
# create UI for SelectDateTime dialog (separate window)
class Ui_SelectDateTime(object):
    def setupUi(self, SelectDateTime):
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
"color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(85, 170, 255);\n"
"border-color: rgb(170, 85, 0);\n"
"alternate-background-color: rgb(164, 255, 237);")
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
        self.timeEdit.setWrapping(True)
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
        #self.pushButton_Confirm.clicked.connect(self.comfirmClicked)
    def retranslateUi(self, SelectDateTime):
        _translate = QtCore.QCoreApplication.translate
        SelectDateTime.setWindowTitle(_translate("SelectDateTime", "Canteen System"))
        self.label_titleDate.setText(_translate("SelectDateTime", "Set Preferred Date"))
        self.label_titleTime.setText(_translate("SelectDateTime", "Set Preferred Time"))
        self.pushButton_Back.setText(_translate("SelectDateTime", "Back"))
        self.pushButton_Confirm.setText(_translate("SelectDateTime", "Confirm"))


class SelectDateTime(QtWidgets.QDialog, Ui_SelectDateTime):
    # initialise dialog window and connect functions with the buttons
    def __init__(self,mainWindowController):
        super(SelectDateTime, self).__init__()
        self.setupUi(self)
        
        # initialise mainWindowController 
        self.mainWindowController=mainWindowController

        # when Confirm button is clicked, set system's date and time as chosen by the user
        self.pushButton_Confirm.clicked.connect(self.confirmClicked)

        # when Confirm button is clicked, close the dialog window
        self.pushButton_Confirm.clicked.connect(self.close)
        # when Back button is clicked, close the dialog window
        self.pushButton_Back.clicked.connect(self.close)
    
    # this function is to obtain a string of user's selected date and time, 
    # and convert it to datetime object in python to set as system's datetime
    def confirmClicked(self):
        # convert date and time chosen by user into one string
        dateTimeString=self.userChosenDate()+' '+self.userChosenTime()
        # set the chosen date and time as the system's date and time
        self.mainWindowController.setSelectTime(datetime.strptime(dateTimeString,'%d/%m/%Y %H:%M:%S'))

    # this function is to return user chosen date from the calendarWidget widget
    def userChosenDate(self):
        # obtain selected date from calendar widget and convert it to string
        date = self.calendarWidget.selectedDate().toString("dd/MM/yyyy")
        #print(self.date)  # for checking in terminal
        return date
        # example: returns 13/10/2019

    # this function is to return user chosen time from the timeWidget
    def userChosenTime(self):
        # obtain selected time from timeEdit widget and convert it to string
        time = self.timeEdit.time().toString("HH:mm:ss")
        #print(self.time)  # for checking in terminal
        return time
        # example: returns 12:00 if user selects 12:00 / 12:00 PM
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SelectDateTimeDialog = SelectDateTime('h')
    SelectDateTimeDialog.show()
    sys.exit(app.exec_())
