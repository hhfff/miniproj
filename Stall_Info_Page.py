# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
from canteen_modal import Stall
from DigitalClockWidget import DigitalClock
import random

'''Left to do:
    - Need label for selected time and date?
    - If statement for selected time | else do curret 
    - Append menu items and stuff from database'''


# need write if statement for selected time

# gets the only the hour and set string to int eg. 24-string to 24-integer
# now = datetime.now()
# int_hourTime = int(now.strftime("%H"))

# using the hour to set random waiting time from 5 to 10 mins if peakhour and 2 to 5 min if non peak hour


# UI generated by PYQT5 Designer
class Ui_Stall_Info_Window(object):
    def setupUi(self, Stall_Info_Window, stall, mainWindowController):
        self.mainWindowController = mainWindowController
        self.stall = stall
        # get stall all operations and menuitems
        self.stall.fetchAllOperationHours()
        self.selectedDatetime = mainWindowController.selectedDateTime
        self.stall.fetchMenuByDay(mainWindowController.getDayIdByDateTime(self.selectedDatetime),
                                  mainWindowController.getTimeByDateTime(self.selectedDatetime))
        int_hourTime = int(self.selectedDatetime.strftime("%H"))
        if int_hourTime >= 7 and int_hourTime < 9:
            self.int_avgWaittime = random.randint(2, 5)
        elif int_hourTime >= 12 and int_hourTime < 14:
            self.int_avgWaittime = random.randint(4, 5)
        elif int_hourTime >= 17 and int_hourTime < 19:
            self.int_avgWaittime = random.randint(2, 5)
        else:
            self.int_avgWaittime = random.randint(1, 3)
        self.str_avgWaittime = str(self.int_avgWaittime)

        self.Stall_Info_Window = Stall_Info_Window
        Stall_Info_Window.setObjectName("Stall_Info_Window")
        Stall_Info_Window.setEnabled(True)
        Stall_Info_Window.setFixedSize(832, 817)
        self.centralwidget = QtWidgets.QWidget(Stall_Info_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.windowFrame = QtWidgets.QFrame(self.centralwidget)
        self.windowFrame.setGeometry(QtCore.QRect(0, -10, 821, 801))
        self.windowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.windowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.windowFrame.setObjectName("windowFrame")

        self.btn_calcWaitTime = QtWidgets.QPushButton(self.windowFrame)
        self.btn_calcWaitTime.setGeometry(QtCore.QRect(660, 740, 141, 41))
        self.btn_calcWaitTime.setObjectName("btn_calcWaitingTime")

        # when Calculate Waiting Time button is clicked, calc_Waittime function is called
        self.btn_calcWaitTime.clicked.connect(self.calc_Waittime)
        
        # instantiate widget object for current date and time (DigitalClockWidget) and set geometry of widget
        self.gridLayoutWidget_DigitalClock = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_DigitalClock.setGeometry(QtCore.QRect(150, 0, 500, 50))
        self.gridLayoutWidget_DigitalClock.setObjectName("gridLayoutWidget_2")

        # create grid for DigitalClockWidget
        self.gridLayout_CurrentDateTime = QtWidgets.QGridLayout(self.gridLayoutWidget_DigitalClock)
        self.gridLayout_CurrentDateTime.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_CurrentDateTime.setObjectName("gridLayout_CurrentDateTime")

        # instantiate DigitalClock widget 
        self.DigitalClockWidget = DigitalClock(self.mainWindowController)
        # add DigitalClock widget into grid
        self.gridLayout_CurrentDateTime.addWidget(self.DigitalClockWidget)
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.windowFrame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 791, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.stallGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.stallGrid.setContentsMargins(0, 0, 0, 0)
        self.stallGrid.setHorizontalSpacing(12)
        self.stallGrid.setVerticalSpacing(2)
        self.stallGrid.setObjectName("stallGrid")
        self.label_stallDesc = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_stallDesc.setObjectName("label_stallDesc")
        self.stallGrid.addWidget(self.label_stallDesc, 1, 0, 1, 1)
        self.label_stallName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_stallName.setObjectName("label_stallName")
        self.stallGrid.addWidget(self.label_stallName, 0, 0, 1, 1)
        self.label_stallOpHour = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_stallOpHour.setObjectName("label_stallOpHour")
        self.stallGrid.addWidget(self.label_stallOpHour, 2, 0, 1, 1)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.windowFrame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 280, 791, 291))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.menuGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.menuGrid.setContentsMargins(0, 0, 0, 0)
        self.menuGrid.setSpacing(10)
        self.menuGrid.setObjectName("menuGrid")

        self.label_menu_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_menu_title.setMaximumSize(QtCore.QSize(12500, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_menu_title.setFont(font)
        self.label_menu_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_menu_title.setIndent(6)
        self.label_menu_title.setObjectName("label_menu_title")
        self.menuGrid.addWidget(self.label_menu_title, 0, 0, 1, 1)

        self.label_price_title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_price_title.setFont(font)
        self.label_price_title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_price_title.setIndent(15)
        self.label_price_title.setObjectName("label_price_title")
        self.menuGrid.addWidget(self.label_price_title, 0, 1, 1, 1)
        self.list_menu_items = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.list_menu_items.setObjectName("list_menu_items")
        self.menuGrid.addWidget(self.list_menu_items, 1, 0, 1, 1)
        self.list_price_details = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.list_price_details.setObjectName("list_price_details")
        self.menuGrid.addWidget(self.list_price_details, 1, 1, 1, 1)
        self.menuGrid.setColumnStretch(0, 5)
        self.line = QtWidgets.QFrame(self.windowFrame)
        self.line.setGeometry(QtCore.QRect(-10, 260, 981, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.windowFrame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 570, 791, 151))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.wait_timeGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.wait_timeGrid.setContentsMargins(0, 0, 0, 0)
        self.wait_timeGrid.setObjectName("wait_timeGrid")
        self.label_numPeople = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_numPeople.setObjectName("label_numPeople")
        self.wait_timeGrid.addWidget(self.label_numPeople, 1, 0, 1, 1)
        self.textbox_userIP_numPpl = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.textbox_userIP_numPpl.setObjectName("textbox_userIP_numPpl")
        self.wait_timeGrid.addWidget(self.textbox_userIP_numPpl, 1, 1, 1, 1)
        self.label_calcWaitTime = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_calcWaitTime.setObjectName("label_calcWaitTime")
        self.wait_timeGrid.addWidget(self.label_calcWaitTime, 2, 0, 1, 1)
        self.label_avgWait = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_avgWait.setObjectName("label_avgWait")
        self.wait_timeGrid.addWidget(self.label_avgWait, 0, 0, 1, 1)
        self.label_resultWaitTime = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_resultWaitTime.setText("")
        self.label_resultWaitTime.setObjectName("label_resultWaitTime")
        self.wait_timeGrid.addWidget(self.label_resultWaitTime, 2, 1, 1, 1)

        Stall_Info_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Stall_Info_Window)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 21))
        self.menubar.setObjectName("menubar")
        Stall_Info_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Stall_Info_Window)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        Stall_Info_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Stall_Info_Window)
        menuItem_str = ''
        price_str = ''
        for menuItem in self.stall.menu_items_by_day:
            menuItem_str = menuItem_str + menuItem.name + "\n"
            price_str = price_str + "${}\n".format(menuItem.price)
        print(menuItem_str)
        print(price_str)
        self.list_menu_items.setText(menuItem_str)
        self.list_price_details.setText(price_str)
        QtCore.QMetaObject.connectSlotsByName(Stall_Info_Window)

    def retranslateUi(self, Stall_Info_Window):
        _translate = QtCore.QCoreApplication.translate

        # fetch Stall information from canteen_modal
        currentTime = datetime.now().strftime("%H:%M:%S")  # to get current Time once

        self.label_stallName.setText(_translate("Stall_Info_Window", "Stall Name: " + self.stall.name))
        self.label_stallDesc.setText(_translate("Stall_Info_Window", "Description: " + self.stall.description))
        self.label_stallOpHour.setText(
            _translate("Stall_Info_Window", "Full Operation Hours:\n" + self.stall.getAllOperationHoursInString()))

        # self.list_menu_items.append()
        self.label_calcWaitTime.setText("Estimated Waiting Time: ")
        self.label_calcWaitTime.hide()
        self.label_resultWaitTime.hide()

        # generated by PYQT5 Designer
        Stall_Info_Window.setWindowTitle(_translate("Stall_Info_Window", "Stall Page"))
        self.btn_calcWaitTime.setText(_translate("Stall_Info_Window", "Calculate Waiting Time"))
        self.label_menu_title.setText(_translate("Stall_Info_Window", "Menu"))
        self.label_price_title.setText(_translate("Stall_Info_Window", "Price"))
        # self.btn_calcWaitTime.setText(_translate("Stall_Info_Window", "Calculate Waiting Time"))
        self.label_avgWait.setText(
            _translate("Stall_Info_Window", "Average waiting time per person: " + self.str_avgWaittime + " minutes"))
        self.label_numPeople.setText(_translate("Stall_Info_Window", "Number of people in queue: "))
        self.textbox_userIP_numPpl.setPlaceholderText("Type number of people in Queue")

    # from button calculate waiting time  clicked
    def calc_Waittime(self):

        # try, except for ValueError
        try:
            # convert user input to int
            userInput_Ppl = int(self.textbox_userIP_numPpl.text())

            # if user inputs less than 0, error message pop up
            if userInput_Ppl < 0:
                self.error_message("\nPlease input a positive number")

            # if user inputs more than 100, error message pop up
            elif userInput_Ppl >= 100:
                self.error_message("\nPlease input lesser than 100 people ")

            # if user inputs 0
            elif userInput_Ppl == 0:
                self.label_calcWaitTime.show()
                self.label_resultWaitTime.show()
                self.label_resultWaitTime.setText(" 0 minutes - no one in queue")

            # if all conditions met caclculate waiting time and show the label
            else:
                result = str(self.int_avgWaittime * userInput_Ppl)
                self.label_calcWaitTime.show()
                self.label_resultWaitTime.show()
                self.label_resultWaitTime.setText(result + " minutes")

        # if user does not input any value or inputs non integer or fractions
        except ValueError:
            self.error_message("\nPlease input numeric integer between 0 - 100")

    # function to show error message, function requires parameter of error message to show
    def error_message(self, message):
        # disable Stall Page
        # self.Stall_Info_Window.setEnabled(False)

        # create error pop uop
        # q messagebox auto block parent window
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error!!!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

        # hide calculated label, clear user inputted text, enable Stall Page after user click ok
        ##self.label_resultWaitTime.hide()
        # self.textbox_userIP_numPpl.setText("")
        # self.Stall_Info_Window.setEnabled(True)
        # return()

    # function to do when home button is clicked, no parameter is required
    def func_home(self):
        # Stall_Info_Window.close()
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Stall_Info_Window = QtWidgets.QMainWindow()
    ui = Ui_Stall_Info_Window()
    ui.setupUi(Stall_Info_Window, 'h', 'main')

    Stall_Info_Window.show()
    sys.exit(app.exec_())
