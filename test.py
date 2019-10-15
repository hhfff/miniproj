from canteen_modal import Canteen
from canteen_modal import Stall
from canteen_modal import Day
import db




db.check_DB_exist()
#use calenday to get day like Monday, change it to id
#only class has corresponding database table  can use all(),otherwise will throw error
days=Day.all()
for i in days:
    print(f'{i.id}\t{i.name}')#hi
today='Tuesday'
for i in days:
    if i.name==today:
        today=i
print(today.name)

stalls=Stall.fetchStalls(today.id,'12:00:00') #only 3rd stall has menu
print('-------------stalls------------')
for i in stalls:
    print(i.name)
    '''for y in i.stall_types:
        print(y,end='\t')'''
print()

#fetch stalls data
stall=stalls.pop()
op=stall.operation_hour
print(op.name,op.start_time,op.end_time)

stall.fetchAllOperationHours()
for i in stall.all_operation_hours:
    print(i.name,i.start_time,i.end_time)
    
#fetch menus
print(stall.name)
stall.fetchMenuByDay(today.id,'14:35:00')
for i in stall.menu_items_by_day:
    print(f'{i.name}\t{i.price}\t{i.food_types}\t{i.operation_hour.name}\t{i.operation_hour.start_time}\t{i.operation_hour.end_time}')



