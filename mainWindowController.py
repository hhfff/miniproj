import datetime
import calendar
from canteen_modal import Canteen, Stall
import db

class MainWindowController():

    def __init__(self,mainUi):
        db.check_DB_exist()
        self.mainUi=mainUi
        self.image_url_prefix='images/'
        self.currentDatetime=self.getCurrentSystemTime()
        self.selectedDateTime=self.currentDatetime
        #self.selectedDateTime=datetime.fromtimestamp(self.currentDatetime.)
        self.canteen=Canteen.all()[0]
        self.all_stalls=[]
        self.getStalls(self.selectedDateTime)
        
        #self.selectedDateTime=datetime.datetime.fromtimestamp(self.currentDatetime)

    def getCurrentSystemTime(self):
        return datetime.datetime.now()
    
    def getDayIdByDateTime(self,datetime):
        #monday is 0, but in database is 1 so plus 1
        return datetime.weekday()+1
    def getTimeByDateTime(self,datetime):
        return datetime.strftime('%H:%M:%S')
        #return '09:09:09'

    def getStalls(self,datetime):
        self.curr_stalls=Stall.fetchStalls(self.getDayIdByDateTime(datetime),self.getTimeByDateTime(datetime))

    def setSelectTime(self,newValue):
        #todo check equal
        self.selectedDateTime=newValue
        self.getStalls(self.selectedDateTime)
        self.mainUi.updateDateTimeText(self.selectedDateTime.strftime("%m/%d/%Y %H:%M:%S"))
        self.mainUi.displayStall()
    

    
        
