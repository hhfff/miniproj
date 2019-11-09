import db
class BaseObject:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        
    @classmethod
    def all(cls):
        target_class=globals()[cls.__name__]
        result=db.retrieve('select * from {}'.format((cls.__name__+'s').lower()))
        return [target_class(data) for data in result]
         
    def findById(self,id):
        pass
        
    def first(self):
        pass
    def last(self):
        pass
#python has multiple inheritance
class ItemType(BaseObject):
    def __init__(self,id,name,description,pic_addr):
        super().__init__(id,name)
        self.description=description
        self.pic_addr=pic_addr

class FoodType(BaseObject):
    def __init__(self,data):
        super().__init__(data['id'],data['name'])

class StallType(BaseObject):
    def __init__(self,data):
        super().__init__(data['id'],data['name'])

class Day(BaseObject):
    def __init__(self,data):
        super().__init__(data['id'],data['name'])
class OperationHour(Day):
    def __init__(self,id,name,start_time,end_time):
        super().__init__({'id':id,'name':name})
        self.start_time=start_time
        self.end_time=end_time

class CanteenType(BaseObject):
    def __init__(self,data):
        super().__init__(data['id'],data['name'])

class Canteen(ItemType):
    #may be dict is better choice for data
    def __init__(self,data):
        super().__init__(data['id'],data['name'],data['description'],data['pic_addr'])

class Stall(ItemType):
    #menuitems
    
    def __init__(self,data):
        #id,name,description,pic_addr,average_waiting_time,operation_hour
        super().__init__(data['id'],data['name'],data['description'],data['pic_addr'])
        self.all_operation_hours=[]
        #self.average_waiting_time=data['average_waiting_time']
        self.canteen_id=data['canteen_id']
        self.operation_hour=OperationHour(data['day_id'],data['day_name'],data['start_time'],data['end_time'])
        self.stall_types=data['stall_type'].split(',')

        self.menu_items_by_day=[] 

    @staticmethod
    def fetchStalls(day_id,time):
        #each store only has 1 store type, if not must use group concat
        query='''select stalls.id,stalls.name,stalls.description,stalls.pic_addr,stalls.canteen_id,operation_hours.day_id,days.name as day_name,operation_hours.start_time,operation_hours.end_time, stall_types.name as stall_type from stalls
            inner join operation_hours 
            on stalls.id = operation_hours.stall_id
            inner join days 
            on operation_hours.day_id=days.id
			INNER JOIN stall_stall_types
			on stalls.id=stall_stall_types.stall_id
			INNER JOIN stall_types
			on stall_stall_types.stall_type_id=stall_types.id
            where operation_hours.day_id={}
            and time(operation_hours.start_time)<= time('{}')
            and time('{}') <=time(operation_hours.end_time) order by stalls.name'''.format(day_id,time,time)
        #result will be list of dictionary, below
        #{'id': 1, 'name': 'Chicken Rice', 'description': 'Tender chicken', 'piame,start_time,end_time,picc_addr': '', 'canteen_id': 1, 'day_id': 1, 'day_name': 'Monday', 'start_time': '09:30:00', 'end_time': '19:30:00'}
        result=db.retrieve(query)
        return [Stall(data) for data in result]

    def fetchAllOperationHours(self):
        if len(self.all_operation_hours) <=0:
            query='''select operation_hours.day_id, days.name,operation_hours.start_time,operation_hours.end_time from operation_hours
                    inner join days
                    on operation_hours.day_id=days.id
                    where stall_id={};
            '''.format(self.id)
            rs=db.retrieve(query)
            [self.all_operation_hours.append(OperationHour(data['day_id'],data['name'],data['start_time'],data['end_time'])) for data in rs]
    def getAllOperationHoursInString(self):
        str=''
        for operationHour in self.all_operation_hours:
            s="{} {} - {}\n".format(operationHour.name,operationHour.start_time,operationHour.end_time)
            str+=s
        return str

    def fetchMenuByDay(self,day_id,time):
        #todo
        #menu item items column does't require
        
        query='''SELECT menu_items.id,menu_items.name,menu_items.description,menu_items.pic_addr,menu_items.price,menu_items.stall_id,menu_items_time.day_id, days.name as day_name,menu_items_time.start_time,menu_items_time.end_time from menu_items 
                INNER JOIN menu_items_time 
                on menu_items.id=menu_items_time.menu_item_id
                INNER JOIN days
                on menu_items_time.day_id=days.id
                WHERE menu_items.stall_id={}
                AND days.id={}
                AND time(menu_items_time.start_time)<='{}'
                AND '{}'<=time(menu_items_time.end_time)
                order by menu_items.name
                ;
        '''.format(self.id,day_id,time,time)
        self.menu_items_by_day=[ MenuItem(data) for data in db.retrieve(query)]
        
    def fetchAllMenu(self):
        pass
        

class MenuItem(ItemType):
    def __init__(self,data):
        super().__init__(data['id'],data['name'],data['description'],data['pic_addr'])
        self.price=data['price']
        self.stall_id=data['stall_id']
        #self.food_types=data['food_type'].split(',')
        self.operation_hour=OperationHour(data['day_id'],data['day_name'],data['start_time'],data['end_time'])




