import sqlite3
DB_NAME='data.db'
#should just dump data from database
sqls='''
        create table if not exists canteens(
            id integer primary key,
            name text not null,
            description text,
            pic_addr text
        );
        insert into canteens (name,description,pic_addr) values('North spine canteen','canteen','');
        create table if not exists food_types(
            id integer primary key,
            name text not null
        );
        insert into food_types(name) values ('chinese');
        insert into food_types(name) values ('western');
        insert into food_types(name) values ('Soup');
        

        create table if not exists menu_item_food_types(
            menu_item_id integer,
            food_type_id integer,
            primary key(menu_item_id,food_type_id),
            foreign key(menu_item_id) references menu_items(id)
            foreign key(food_type_id) references food_types(id)
        );


        create table if not exists stall_types(
            id integer primary key,
            name text not null
        );
        insert into stall_types(name) values ('hala');
        insert into stall_types(name) values ('non-hala');
        insert into stall_types(name) values ('Fast food');
        
        create table if not exists stall_stall_types(
            stall_id integer,
            stall_type_id integer,
            primary key(stall_id,stall_type_id),
            foreign key(stall_id) references stalls(id)
            foreign key(stall_type_id) references stall_types(id)
            
        );
        create table if not exists days(
            id integer primary key,
            name text not null
        );
        insert into days(name) values ('Monday');
        insert into days(name) values ('Tuesday');
        insert into days(name) values ('Wednesday');
        insert into days(name) values ('Thursday');
        insert into days(name) values ('Friday');
        insert into days(name) values ('Saturday');
        insert into days(name) values ('Sunday');

        

        create table if not exists stalls(
            id integer primary key,
            name text not null,
            description text,
            pic_addr text,
            canteen_id integer,
            foreign key(canteen_id) references canteens(id)
        );
        

        insert into stalls (name,description,pic_addr,canteen_id) values('Chicken Rice','Tender chicken','',1);
        insert into stall_stall_types(stall_id, stall_type_id) values(1,2);
        
        insert into stalls (name,description,pic_addr,canteen_id) values('Malay food','malay food descript','',1);
        insert into stall_stall_types(stall_id, stall_type_id) values(2,1);

        insert into stalls (name,description,pic_addr,canteen_id) values('McDonald','various drink','',1);
        insert into stall_stall_types(stall_id, stall_type_id) values(3,1);
        insert into stall_stall_types(stall_id, stall_type_id) values(3,3);

        create table if not exists operation_hours(
            stall_id integer,
            day_id integer  ,         
            start_time text,
            end_time text,
            primary key(stall_id,day_id,start_time,end_time),
            foreign key(stall_id) references stalls(id),
            foreign key(day_id) references days(id)
        );
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(1,1,'09:30:00','19:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(1,2,'09:30:00','19:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(1,3,'09:30:00','19:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(1,4,'09:30:00','19:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(1,5,'09:30:00','19:30:00');

        insert into operation_hours (stall_id,day_id,start_time,end_time) values(2,1,'09:00:00','19:00:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(2,2,'09:30:00','19:00:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(2,4,'09:30:00','19:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(2,5,'09:00:00','19:30:00');

        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,1,'09:30:00','21:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,2,'09:30:00','21:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,3,'09:30:00','21:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,4,'09:30:00','21:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,5,'09:30:00','21:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,6,'09:30:00','21:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,7,'09:30:00','21:30:00');
        
        create table if not exists menu_items(
            id integer primary key,
            name text not null,
            description text,
            pic_addr text,
            price real,
            stall_id integer,
            foreign key(stall_id) references stalls(id)
        );
        insert into menu_items(name,description,pic_addr,price,stall_id) values(
            'Cheesebuger',
            'Start with a perfect McDonald''s Hamburger. Put warm, melting cheese on the patty and take the experience to the next level. Need we say more?',
            '',
            6.5,
            3
            );
        
        insert into menu_items(name,description,pic_addr,price,stall_id) values(
            'The Original Angus',
            'Made from all the things you love two slices of melty cheese, slivered onions and 100% Angus beef. All between aromatic glazed buns for an irresistible finish.',
            '',
            7,
            3
        );
        insert into menu_item_food_types values(1,2);
        insert into menu_item_food_types values(2,2);
        insert into menu_item_food_types values(2,1);

        create table if not exists menu_items_time(
            menu_item_id integer,
            day_id integer  ,         
            start_time text,
            end_time text,
            primary key(menu_item_id,day_id,start_time,end_time),
            foreign key(menu_item_id) references menu_items(id),
            foreign key(day_id) references days(id)
        );
        --cheese burger
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(1,1,'09:30:00','21:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(1,2,'09:30:00','21:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(1,3,'09:30:00','21:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(1,4,'09:30:00','21:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(1,6,'09:30:00','21:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(1,7,'09:30:00','21:30:00');
        --The Original Angus
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(2,1,'14:30:00','21:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(2,2,'14:30:00','21:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(2,3,'14:30:00','21:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(2,4,'14:30:00','21:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(2,5,'14:30:00','21:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(2,6,'14:30:00','21:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(2,7,'14:30:00','21:30:00');
        
        '''

def check_DB_exist():
    try:
        conn=sqlite3.connect(DB_NAME)
        cursor=conn.cursor()
        cursor.execute('select * from canteens')

    except Exception as e:
        initDB()
    finally:
        conn.close()
def initDB():
    try:
        conn=sqlite3.connect(DB_NAME)
        cursor=conn.cursor()
        cursor.executescript(sqls)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        conn.close()
def insert():
    pass
def retrieve(query):
    #print(query)
    try:
        conn=sqlite3.connect(DB_NAME)
        cursor=conn.cursor()
        cursor.execute(query)
        desc=cursor.description
        column_names = [col[0] for col in desc]
        #dictionary type, map column name with data
        return [dict(zip(column_names,row)) for row in cursor.fetchall()] #a,b,c,d 1,2  -> a1,b1, if want c,d use izip_long
    except Exception as e:
        print(e)
    finally:
        conn.close()
        
def update():
    pass
def delete():
    pass



