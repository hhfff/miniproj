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

    #return Monday to Sunday in integer
    def getDayIdByDateTime(self,datetime):
        #monday is 0, but in database is 1 so plus 1
        return datetime.weekday()+1
    #return datetime in time formate
    def getTimeByDateTime(self,datetime):
        return datetime.strftime('%H:%M:%S')
        #return '09:09:09'

    def getStalls(self,datetime):
        self.curr_stalls=Stall.fetchStalls(self.getDayIdByDateTime(datetime),self.getTimeByDateTime(datetime))
        
    def useCurrentDateTime(self):
        self.currentDatetime=self.getCurrentSystemTime()
        self.setSelectTime(self.currentDatetime)

    #set select time to newValue and update in UI
    def setSelectTime(self,newValue):
        self.selectedDateTime=newValue
        self.getStalls(self.selectedDateTime)
        self.mainUi.updateDateTimeText(self.selectedDateTime)
        self.mainUi.onSearchTextChange()
        
    #non hala,fast food and halal , but since we only has fast food and other, we just compare 2 condition
    def filterStall(self, text, fastfoodChecked, nonfastFoodChecked):
        filteredStall = []  # reset
        for stall in self.curr_stalls:
            if stall.name.lower().find(text.lower()) != -1:
                if fastfoodChecked:
                    if stall.stall_types[0] == 'Fast Food':
                        filteredStall.append(stall)
                if nonfastFoodChecked:
                    if stall.stall_types[0] != 'Fast Food':
                        filteredStall.append(stall)

        self.mainUi.displayStall(filteredStall)
        
        
        

    

    
        
