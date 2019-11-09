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
    def useCurrentDateTime(self):
        self.currentDatetime=self.getCurrentSystemTime()
        self.setSelectTime(self.currentDatetime)

    def setSelectTime(self,newValue):
        #todo check equal
        self.selectedDateTime=newValue
        self.getStalls(self.selectedDateTime)
        self.mainUi.updateDateTimeText(self.selectedDateTime)
        self.mainUi.onSearchTextChange()
        
    #non hala,fast food and halal , but since we only has fast food and other
    def filterStore(self,text,fastfoodChecked,nonfastFoodChecked):
        filteredStore=[] #reset
        for store in self.curr_stalls:
            if store.name.lower().find(text.lower()) !=-1:
                if fastfoodChecked:
                    if store.stall_types[0]=='Fast Food':
                        filteredStore.append(store)
                if nonfastFoodChecked:
                    if store.stall_types[0]!='Fast Food':
                        filteredStore.append(store)
                
            
        self.mainUi.displayStall(filteredStore)
        
        
        

    

    
        
