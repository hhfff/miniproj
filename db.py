import sqlite3

DB_NAME = 'data.db'
# should just dump data from database
sqls = '''
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
        insert into food_types(name) values ('Chinese');
        insert into food_types(name) values ('Western');
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
        insert into stall_types(name) values ('Halal');
        insert into stall_types(name) values ('Non-Halal');
        insert into stall_types(name) values ('Fast Food');
        
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
        

        insert into stalls (name,description,pic_addr,canteen_id) values('Chicken Rice','Tender chicken','chicken_rice.jpg',1);
        insert into stall_stall_types(stall_id, stall_type_id) values(1,2);
        
        insert into stalls (name,description,pic_addr,canteen_id) values('Malay BBQ','Malay cuisines','malay_food.jpeg',1);
        insert into stall_stall_types(stall_id, stall_type_id) values(2,1);

        insert into stalls (name,description,pic_addr,canteen_id) values('McDonalds','Burgers, drinks, snacks and desserts','mcdonalds.jpg',1);
        insert into stall_stall_types(stall_id, stall_type_id) values(3,3);
        
        insert into stalls (name,description,pic_addr,canteen_id) values('Hand-made Noodles','Freshly cooked noodles','banmian.jpg',1);
        insert into stall_stall_types(stall_id, stall_type_id) values(4,2);

        insert into stalls (name,description,pic_addr,canteen_id) values('KFC','Kentucky Fried chicken, burgers and rice bowls','kfc.jpg',1);
        insert into stall_stall_types(stall_id, stall_type_id) values(5,3);
        

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
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(2,2,'09:30:00','19:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(2,4,'09:30:00','19:00:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(2,5,'09:00:00','19:30:00');

        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,1,'07:00:00','23:59:59');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,2,'07:00:00','23:59:59');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,3,'07:00:00','23:59:59');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,4,'07:00:00','23:59:59');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,5,'07:00:00','23:59:59');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,6,'07:00:00','23:59:59');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(3,7,'10:00:00','22:00:00');
        
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(4,1,'08:30:00','20:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(4,2,'08:30:00','20:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(4,3,'08:30:00','20:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(4,4,'08:30:00','20:30:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(4,5,'08:30:00','19:00:00');
		insert into operation_hours (stall_id,day_id,start_time,end_time) values(4,6,'08:30:00','17:00:00');
		
		insert into operation_hours (stall_id,day_id,start_time,end_time) values(5,1,'11:00:00','20:00:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(5,2,'11:00:00','20:00:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(5,3,'11:00:00','20:00:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(5,4,'11:00:00','20:00:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(5,5,'11:00:00','20:00:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(5,6,'11:00:00','20:00:00');
        insert into operation_hours (stall_id,day_id,start_time,end_time) values(5,7,'11:00:00','20:00:00');

        
        create table if not exists menu_items(
            id integer primary key,
            name text not null,
            description text,
            pic_addr text,
            price real,
            stall_id integer,
            foreign key(stall_id) references stalls(id)
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'Cheeseburger',
            'Start with a perfect McDonald''s Hamburger. Put warm, melting cheese on the patty and take the experience to the next level. Need we say more?',
            '',
            6.5,
            3
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'The Original Angus',
            'Made from all the things you love two slices of melty cheese, slivered onions and 100% Angus beef. All between aromatic glazed buns for an irresistible finish.',
            '',
            7,
            3
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'McSpicy', 
            'If you are one of those people who like your chicken big on spiciness, this is the sandwich for you. A thick, juicy cutlet of chicken thigh and drum sits fiery hot on a bed of crunchy lettuce between toasted sesame seed buns – shiok!', 
            '', 
            7, 
            3
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'Sausage McMuffin with egg',
            'Sumptuous chicken sausage and an egg done sunny side-up served between perfectly toasted muffins.',
            '',
            4.50,
            3
        );
        
        insert into menu_items(name,description,pic_addr,price,stall_id) values(
            'Roasted Chicken Rice', 
            'Roasted chicken cut into bite-size pieces and served on fragrant rice.',
            '',
            3,
            1
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'Steamed Chicken Rice', 
            'Steamed chicken cut into bite-size pieces and served on fragrant rice.',
            '',
            3,
            1
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'Chicken Horfun', 
            'Freshly cut bite-sized chicken served on piping hot horfun.',
            '',
            3,
            1
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'Mee Rebus with Satay Stick', 
            'Chinese egg noodles in thick, spicy gravy and barbecued beef satay sticks',
            '',
            4.50,
            2
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'Nasi Lemak with BBQ Chicken',
            'Freshly made grilled chicken in thick barbecue sauce served with coconut rice, egg, ikan bilis, nuts and slices of cucumber.',
            '',
            4,
            2
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'Lontong',
            'Compressed rice cakes, cabbage and boiled egg served in hot curry.',
            '',
            2.50,
            2
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'Ban Mian/U Mian',
            'Egg noodles served in a flavorful soup, with minced meat, egg, vegetables and various spices.',
            '',
            3.00,
            4
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'Tom Yum Ban Mian',
            'Egg noodles served in a flavorful spicy and sour tom yum soup, with minced meat, egg, vegetables and various spices.',
            '',
            3.80,
            4
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'Zha Jiang Mian',
            'Egg noodles served in a dry, minced meat bean sauce with egg, vegetables and carrots.',
            '',
            3.80,
            4
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            '3-Piece Chicken Meal',
            '3 pieces of fried chicken (original/crispy) with mashed potatoes, coleslaw and a soft drink.',
            '',
            8.40,
            5
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'Zinger meal',
            'Burger with spicy, crispy fried chicken patty served with fries and a cup of soft drink.',
            '',
            6,
            5
        );
        
        insert into menu_items (name,description,pic_addr,price,stall_id) values(
            'Original Recipe Rice Bowl Meal',
            '1 Bowl of Original Recipe Rice Bowl with bite-sized popcorn chicken, 1 piece chicken (original/crispy) and a cup of soft drink.',
            '',
            8,
            5
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
        
        --Cheeseburger
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
        --McSpicy
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(3,1,'11:00:00','23:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(3,2,'11:00:00','23:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(3,3,'11:00:00','23:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(3,4,'11:00:00','23:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(3,5,'11:00:00','23:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(3,6,'11:00:00','23:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(3,7,'11:00:00','21:30:00');
        --Sausage McMuffin with Egg
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(4,1,'07:00:00','11:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(4,2,'07:00:00','11:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(4,3,'07:00:00','11:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(4,4,'07:00:00','11:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(4,5,'07:00:00','11:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(4,6,'07:00:00','11:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(4,7,'07:00:00','11:00:00');
        --Roasted Chicken Rice
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(5,1,'09:30:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(5,2,'09:30:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(5,3,'09:30:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(5,4,'09:30:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(5,5,'09:30:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(5,1,'17:00:00','19:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(5,2,'17:00:00','19:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(5,3,'17:00:00','19:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(5,4,'17:00:00','19:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(5,5,'17:00:00','19:30:00');
        --Steamed Chicken Rice
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(6,1,'09:30:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(6,2,'09:30:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(6,3,'09:30:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(6,4,'09:30:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(6,5,'09:30:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(6,1,'17:00:00','19:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(6,2,'17:00:00','19:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(6,3,'17:00:00','19:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(6,4,'17:00:00','19:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(6,5,'17:00:00','19:30:00');
        --Chicken Horfun
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(7,1,'09:30:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(7,2,'09:30:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(7,3,'09:30:00','15:00:00');
        --Mee Rebus with Satay Stick
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(8,1,'09:00:00','19:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(8,5,'09:00:00','19:30:00');
        --Nasi Lemak with BBQ Chicken
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(9,1,'09:00:00','14:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(9,2,'09:30:00','14:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(9,4,'15:30:00','19:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(9,5,'15:00:00','19:30:00');
        --Lontong
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(10,1,'09:00:00','19:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(10,2,'09:30:00','19:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(10,4,'09:30:00','19:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(10,5,'09:00:00','19:30:00');
        --Ban Mian/U Mian
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(11,1,'08:30:00','20:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(11,2,'08:30:00','20:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(11,3,'08:30:00','20:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(11,4,'08:30:00','20:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(11,5,'08:30:00','19:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(11,6,'08:30:00','17:00:00');
        --Tom Yum Ban Mian
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(12,1,'08:30:00','20:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(12,2,'08:30:00','20:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(12,3,'08:30:00','20:30:00');
        --Zha Jiang Mian
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(13,4,'08:30:00','20:30:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(13,5,'08:30:00','19:00:00');
        --3-Piece Chicken Meal
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(14,1,'11:00:00','20:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(14,2,'11:00:00','20:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(14,3,'11:00:00','20:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(14,4,'11:00:00','20:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(14,5,'11:00:00','20:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(14,6,'11:00:00','20:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(14,7,'11:00:00','20:00:00');
        --Zinger meal
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(15,1,'14:00:00','20:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(15,2,'14:00:00','20:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(15,3,'14:00:00','20:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(15,4,'14:00:00','20:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(15,5,'14:00:00','20:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(15,6,'14:00:00','20:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(15,7,'14:00:00','20:00:00');
        --Original Recipe Rice Bowl Meal
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(16,1,'11:00:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(16,2,'11:00:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(16,3,'11:00:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(16,4,'11:00:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(16,5,'11:00:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(16,6,'11:00:00','15:00:00');
        insert into menu_items_time (menu_item_id,day_id,start_time,end_time) values(16,7,'11:00:00','15:00:00');
        
        '''


def check_DB_exist():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('select * from canteens')

    except Exception as e:
        initDB()
    finally:
        conn.close()


def initDB():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
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
    dataList=[]
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(query)
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data=cursor.fetchall()
       
        #[(None, None, None, None, None, None, None, None, None, None)], sqlite will return this if no result
        if data[0][0] != None or len(data)!=0:
            
            dataList=[dict(zip(column_names, row)) for row in data]  # a,b,c,d 1,2  -> a1,b1, if want c,d use izip_long
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return dataList

def update():
    pass


def delete():
    pass
