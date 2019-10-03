import datetime
import calendar
class MapytinWindowController():
    def __init__(self):
        self.currentDatetime=self.getCurrentSystemTime()
        self.selectedDateTime=datetime.fromtimestamp(self.currentDatetime)

    def getCurrentSystemTime(self):
        return datetime.datetime.now()
    
    def getDayNameByDate(self,datetime):
        #monday is 0, but in database is 1 so plus 1
        return datetime.weekday()+1


    
        
