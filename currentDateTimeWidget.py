from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget_currentDate_digitalClock(object):
    def setupUi(self, widget_currentDate_digitalClock):
        widget_currentDate_digitalClock.setObjectName("widget_currentDate_digitalClock")
        widget_currentDate_digitalClock.resize(631, 170)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_currentDate_digitalClock.sizePolicy().hasHeightForWidth())
        widget_currentDate_digitalClock.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(widget_currentDate_digitalClock)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_CurrentDate = QtWidgets.QLabel(widget_currentDate_digitalClock)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_CurrentDate.sizePolicy().hasHeightForWidth())
        self.label_CurrentDate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_CurrentDate.setFont(font)
        self.label_CurrentDate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_CurrentDate.setObjectName("label_CurrentDate")
        self.verticalLayout.addWidget(self.label_CurrentDate)
        self.label_DigitalClock = QtWidgets.QLabel(widget_currentDate_digitalClock)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_DigitalClock.sizePolicy().hasHeightForWidth())
        self.label_DigitalClock.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_DigitalClock.setFont(font)
        self.label_DigitalClock.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DigitalClock.setObjectName("label_DigitalClock")
        self.verticalLayout.addWidget(self.label_DigitalClock)

        self.retranslateUi(widget_currentDate_digitalClock)
        QtCore.QMetaObject.connectSlotsByName(widget_currentDate_digitalClock)

    def retranslateUi(self, widget_currentDate_digitalClock):
        _translate = QtCore.QCoreApplication.translate
        widget_currentDate_digitalClock.setWindowTitle(_translate("widget_currentDate_digitalClock", "Canteen System"))
        self.label_CurrentDate.setText(_translate("widget_currentDate_digitalClock", "Current Date"))
        self.label_DigitalClock.setText(_translate("widget_currentDate_digitalClock", "Current Time"))


class OpenDTWidget(QtWidgets.QWidget, Ui_widget_currentDate_digitalClock):
    def __init__(self, parent=None):
        super(OpenDTWidget, self).__init__(parent)
        self.setupUi(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showDate)
        timer.timeout.connect(self.showTime)
        timer.start(100)

    def showDate(self):
        date = QtCore.QDate.currentDate()
        textDate = date.toString("dddd, dd MMMM, yyyy")
        self.label_CurrentDate.setText(textDate)

    def showTime(self):
        time = QtCore.QTime.currentTime()
        textTime = time.toString('hh:mm:ss')
        self.label_DigitalClock.setText(textTime)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget_currentDate_digitalClock = OpenDTWidget()
    widget_currentDate_digitalClock.show()
    sys.exit(app.exec_())
