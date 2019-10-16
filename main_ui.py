# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'canteen.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui,QtWidgets
from mainWindowController import MainWindowController


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #init controller
        self.main_window_controller=MainWindowController()
        #MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground,True)
        #MainWindow.setStyleSheet("background-color:rgba(255,255,255,0.9)")


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        #self.centralwidget.setGraphicsEffect(QtWidgets.QGraphicsBlurEffect())

        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_canteen_name = QtWidgets.QLabel(self.centralwidget)
        self.lbl_canteen_name.setObjectName("lbl_canteen_name")
        self.verticalLayout.addWidget(self.lbl_canteen_name)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ck_normal = QtWidgets.QCheckBox(self.centralwidget)
        self.ck_normal.setObjectName("ck_normal")
        self.verticalLayout_2.addWidget(self.ck_normal)
        self.ck_fast_food = QtWidgets.QCheckBox(self.centralwidget)
        self.ck_fast_food.setObjectName("ck_fast_food")
        self.verticalLayout_2.addWidget(self.ck_fast_food)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_date = QtWidgets.QLabel(self.centralwidget)
        self.lbl_date.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_date.setObjectName("lbl_date")
        self.verticalLayout_4.addWidget(self.lbl_date)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout)


        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 784, 533))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_stalls = QtWidgets.QGridLayout()
        self.gridLayout_stalls.setObjectName("gridLayout_stalls")
        

        '''spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_stalls.addItem(spacerItem, 1, 1, 1, 1)

        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_stalls.addItem(spacerItem1, 1, 0, 1, 1)'''

        self.horizontalLayout_2.addLayout(self.gridLayout_stalls)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.displayStall()
        
            

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.openDateTimePicker)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_canteen_name.setText(_translate("MainWindow", self.main_window_controller.canteen.name))
        self.ck_normal.setText(_translate("MainWindow", "Normal"))
        self.ck_fast_food.setText(_translate("MainWindow", "Fast Food"))
        self.lbl_date.setText(_translate("MainWindow", "date"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def openDateTimePicker(self):
        print('test')
    def loadImage(self,image_url,isIcon=False):
        try:
            if isIcon:
                return QtGui.QIcon(image_url) 
            else:
                return QtGui.QPixmap(image_url)
        except Exception as e:
            print('load image error')

    def displayStall(self):
        for item in self.main_window_controller.curr_stalls:
            print(self.main_window_controller.image_url_prefix+item.pic_addr)
            btn=QtWidgets.QPushButton(item.name)
            btn.setMaximumSize(QtCore.QSize(100,100))
            btn.clicked.connect(self.openStallDetail)
            icon=self.loadImage(self.main_window_controller.image_url_prefix+item.pic_addr,isIcon=True)
            btn.setIcon(icon)
            btn.setStyleSheet('''
            QPushButton{
                background-color:rgb(0,255,0);
                text-align: center;
            }
            QPushButton:hover{
                background-color:rgb(255,0,0);

            }
            ''')
            
            self.gridLayout_stalls.addWidget(btn,0,0)
        x,y=1,0
        for i in range(5):
            self.gridLayout_stalls.addWidget(QtWidgets.QLabel(str(i)),y,x)
            x+=1
            if x>=3:
                y+=1
                x=0

    def openStallDetail(self):
        pass

