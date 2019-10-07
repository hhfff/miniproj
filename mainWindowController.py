import datetime
import calendar
class MapytinWindowController():
    def __init__(self):
        self.currentDatetime=self.getCurrentSystemTime()
        self.selectedDateTime= datetime.datetime.fromtimestamp(self.currentDatetime)

    def getCurrentSystemTime(self):
        return datetime.datetime.now()
    
    def getDayNameByDate(self):
        #monday is 0, but in database is 1 so plus 1
        return datetime.weekday()+1

datetime = datetime.date(year= 2019, month= 10, day= 3)
print(MapytinWindowController.getDayNameByDate(datetime))
#output is 4 (meaning Thursday)    
        
