from PyQt5 import QtCore, QtGui, QtWidgets

## designed by Stanley
class Ui_widget_DigitalClock(object):
    def setupUi(self, widget_DigitalClock):
        widget_DigitalClock.setObjectName("widget_DigitalClock")
        widget_DigitalClock.resize(631, 170)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_DigitalClock.sizePolicy().hasHeightForWidth())
        widget_DigitalClock.setSizePolicy(sizePolicy)

        self.verticalLayout = QtWidgets.QVBoxLayout(widget_DigitalClock)
        self.verticalLayout.setObjectName("verticalLayout")

        '''self.label_Title = QtWidgets.QLabel(widget_DigitalClock)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Title.sizePolicy().hasHeightForWidth())
        self.label_Title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Title.setObjectName("label_Title")
        self.label_Title.setText("Current Date and Time:")
        self.verticalLayout.addWidget(self.label_Title)'''

        '''self.label_CurrentDate = QtWidgets.QLabel(widget_DigitalClock)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_CurrentDate.sizePolicy().hasHeightForWidth())
        self.label_CurrentDate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_CurrentDate.setFont(font)
        self.label_CurrentDate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_CurrentDate.setObjectName("label_CurrentDate")
        self.verticalLayout.addWidget(self.label_CurrentDate)'''

        self.label_DigitalClock = QtWidgets.QLabel(widget_DigitalClock)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_DigitalClock.sizePolicy().hasHeightForWidth())
        self.label_DigitalClock.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_DigitalClock.setFont(font)
        self.label_DigitalClock.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DigitalClock.setObjectName("label_DigitalClock")
        self.verticalLayout.addWidget(self.label_DigitalClock)

        self.retranslateUi(widget_DigitalClock)
        QtCore.QMetaObject.connectSlotsByName(widget_DigitalClock)

    def retranslateUi(self, widget_DigitalClock):
        _translate = QtCore.QCoreApplication.translate
        widget_DigitalClock.setWindowTitle(_translate("widget_DigitalClock", "Canteen System"))
        #self.label_CurrentDate.setText(_translate("widget_DigitalClock", "Current Date"))
        self.label_DigitalClock.setText(_translate("widget_DigitalClock", "Current Time"))


class DigitalClock(QtWidgets.QWidget, Ui_widget_DigitalClock):
    def __init__(self,mainWindowController):
        super(DigitalClock, self).__init__()
        self.setupUi(self)
        self.mainWindowController = mainWindowController

        # open QTimer class to connect showDate and showTime functions
        # this allows the date and time to update itself in constant intervals
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showDateAndTime)
        timer.start(100)

    # get the current date and convert it to string of the applied format, and print it on the label
    def showDateAndTime(self):
        # get current date
        date = QtCore.QDate.currentDate()
        # convert today's date into a string of the format day, date month, year
        # example 06/11/2019
        textDate = date.toString("dddd dd/MM/yyyy")
        # get current time
        time = QtCore.QTime.currentTime()
        # convert current time into a string of the format in hours: minutes: seconds
        # example 16:20:15
        textTime = time.toString('hh:mm:ss')
        # update label_DigitalClock with textDate and textTime string
        # example 06/11/2019 16:20:15
        self.label_DigitalClock.setText('Current Date and Time: ' + textDate + ' ' + textTime)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DigitalClockWidget = DigitalClock(mainWindowController=None)
    DigitalClockWidget.show()
    sys.exit(app.exec_())
