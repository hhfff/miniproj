# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'canteen.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui,QtWidgets
from mainWindowController import MainWindowController
from Stall_Info_Page import Ui_Stall_Info_Window
from SelectDateTimeDialog import SelectDateTime
import qtawesome
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #init controller
        self.main_window_controller=MainWindowController(self)

        #MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground,True)
        #MainWindow.setStyleSheet("background-color:rgba(0,0,0,0.9)")


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        #self.centralwidget.setGraphicsEffect(QtWidgets.QGraphicsBlurEffect())
        self.centralwidget.setObjectName("centralwidget")   
        self.centralwidget.setStyleSheet('''
            #centralwidget{
                
            }
        ''')

        
        
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        

        self.lbl_canteen_name = QtWidgets.QLabel(self.centralwidget)
        self.lbl_canteen_name.setObjectName("lbl_canteen_name")
        self.lbl_canteen_name.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lbl_canteen_name.setStyleSheet('''
        QLabel{
            font-size:25px;
            font-weight:bold;

            }''')
        self.verticalLayout.addWidget(self.lbl_canteen_name)

        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.ck_normal = QtWidgets.QCheckBox(self.centralwidget)
        self.ck_normal.setObjectName("ck_normal")
        self.ck_normal.setChecked(True)
        self.ck_normal.stateChanged.connect(self.onSearchTextChange)
        self.verticalLayout_2.addWidget(self.ck_normal)

        self.ck_fast_food = QtWidgets.QCheckBox(self.centralwidget)
        self.ck_fast_food.setObjectName("ck_fast_food")
        self.ck_fast_food.setChecked(True)
        self.ck_fast_food.stateChanged.connect(self.onSearchTextChange)
        self.verticalLayout_2.addWidget(self.ck_fast_food)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        #select data time button and label
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.lbl_date = QtWidgets.QLabel(self.centralwidget)
        self.lbl_date.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_date.setObjectName("lbl_date")
        self.lbl_date.setStyleSheet('''
            #lbl_date{
                font-size:16px;
            }
        ''')
        self.verticalLayout_4.addWidget(self.lbl_date)
        #select button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("selectButton")
        #reset button
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")

        self.buttonWidget=QtWidgets.QWidget()
        self.buttonHorizonLayout=QtWidgets.QHBoxLayout()
        self.buttonHorizonLayout.addWidget(self.resetButton)
        self.buttonHorizonLayout.addWidget(self.pushButton)
        

        self.buttonWidget.setLayout(self.buttonHorizonLayout)

        self.verticalLayout_4.addWidget(self.buttonWidget)

        self.horizontalLayout.addLayout(self.verticalLayout_4)
        
        self.verticalLayout.addLayout(self.horizontalLayout)

        # search
        self.availableStallLabel = QtWidgets.QLabel()
        self.availableStallLabel.setObjectName("availableStallLabel")
        self.availableStallLabel.setText("Available Stalls")
        self.availableStallLabel.setStyleSheet('''
                #availableStallLabel{
                    font-size:16px;
                }
        ''')
        self.searchAreaHLayout = QtWidgets.QHBoxLayout()
        self.searchAreaHLayout.addWidget(self.availableStallLabel)

        self.searchWidget = QtWidgets.QWidget()
        self.searchHlayout = QtWidgets.QHBoxLayout()
        self.searchIcon = QtWidgets.QLabel(chr(0xf002) + ' ' + 'Search  ')
        self.searchIcon.setFont(qtawesome.font('fa', 16))
        self.searchHlayout.addWidget(self.searchIcon)
        self.searchInput = QtWidgets.QLineEdit()
        self.searchInput.setPlaceholderText("Enter Stall Name")
        self.searchInput.textChanged.connect(self.onSearchTextChange)
        self.searchHlayout.addWidget(self.searchInput)
        self.searchWidget.setLayout(self.searchHlayout)
        self.searchWidget.setFixedWidth(300)
        self.searchAreaHLayout.addWidget(self.searchWidget)


        self.searchAreaWidget=QtWidgets.QWidget()
        self.searchAreaWidget.setLayout(self.searchAreaHLayout)
        self.verticalLayout.addWidget(self.searchAreaWidget)
        self.searchAreaWidget.setObjectName('searchAreaWidget')
        self.searchAreaWidget.setStyleSheet('''
            #searchAreaWidget{
            }
        ''')
        
        self.topAreaWidget=QtWidgets.QWidget()
        self.topAreaWidget.setObjectName("topAreaWidget")
        self.topAreaWidget.setLayout(self.verticalLayout)
        self.topAreaWidget.setStyleSheet('''
            #topAreaWidget{
            }
        ''')
        self.verticalLayout_5.addWidget(self.topAreaWidget)
        self.verticalLayout_5.setSpacing(0)



        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet('''
            #scrollArea{
            }
        ''')
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 784, 550))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_stalls = QtWidgets.QGridLayout()
        self.gridLayout_stalls.setObjectName("gridLayout_stalls")
        


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
            

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.openDateTimePicker)
        self.resetButton.clicked.connect(self.resetDateTime)
        self.updateDateTimeText(self.main_window_controller.selectedDateTime)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.onSearchTextChange()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_canteen_name.setText(_translate("MainWindow", "Welcome to North Spine Canteen Information System!"))
        self.ck_normal.setText(_translate("MainWindow", "Normal (Non-Fast-Food)"))
        self.ck_fast_food.setText(_translate("MainWindow", "Fast-Food"))
        self.lbl_date.setText(_translate("MainWindow", 'datetime'))
        self.pushButton.setText(_translate("MainWindow", "Select date and time"))
        self.resetButton.setText(_translate("MainWindow","Use Current date and time"))

    def openDateTimePicker(self):
        self.SelectDateTime = SelectDateTime( self.main_window_controller)
        self.SelectDateTime.setWindowModality(QtCore.Qt.ApplicationModal)
        #self.SelectDateTime.setWindowModality(QtCore.Qt.ApplicationModal)
        #self.selectDateTimeUi = Ui_SelectDateTime()
        #self.selectDateTimeUi.setupUi(self.SelectDateTime,self.main_window_controller)
        self.SelectDateTime.show()

    def loadImage(self,image_url,isIcon=False):
        try:
            if isIcon:
                return QtGui.QIcon(image_url) 
            else:
                return QtGui.QPixmap(image_url)
        except Exception:
            print('load image error')
    def resetDateTime(self):
        self.main_window_controller.useCurrentDateTime()


    def displayStall(self, stalls):
        # delete previous widget first
        for i in reversed(range(self.gridLayout_stalls.count())):
            item = self.gridLayout_stalls.itemAt(i)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                    widget.deleteLater()
        # add new button
        if len(stalls) != 0:
            x, y = 0, 0  # x and y position
            maxX = 3  # maxmum per row
            for item in stalls:
                btn = QtWidgets.QToolButton()
                btn.setText(item.name)
                # btn.setMaximumSize(QtCore.QSize(100,100))
                btn.clicked.connect(lambda checked, item=item: self.openStallDetail(item))
                icon = self.loadImage(self.main_window_controller.image_url_prefix + item.pic_addr, isIcon=True)
                btn.setIcon(icon)
                btn.setIconSize(QtCore.QSize(150, 150))
                btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

                self.gridLayout_stalls.addWidget(btn, y, x)
                x += 1
                if x == maxX:
                    x = 0
                    y += 1
        else:
            label = QtWidgets.QLabel()
            label.setText("No stall available")
            label.setStyleSheet('''
                QLabel{
                    font-size:20px;
                }
            ''')
            label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.gridLayout_stalls.addWidget(label, 0, 0)
       

    def openStallDetail(self,stall):
        self.Stall_Info_Window = QtWidgets.QMainWindow()
        self.Stall_Info_Window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.stallDetail = Ui_Stall_Info_Window()
        self.stallDetail.setupUi(self.Stall_Info_Window,stall,self.main_window_controller)
        self.Stall_Info_Window.show()

    def updateDateTimeText(self,dt):
        self.lbl_date.setText(dt.strftime('%A %d/%m/%Y %H:%M'))
    def onSearchTextChange(self):
        self.main_window_controller.filterStall(self.searchInput.text(), self.ck_fast_food.isChecked(),
                                                self.ck_normal.isChecked())


