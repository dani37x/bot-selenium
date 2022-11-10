from project_files.bot import Cars
from project_files.config import config
from project_files.functions import connection, create_database, create_table, data_send, send_SMS
from project_files.query import DB_NAME, TABLES, add_new_row, add_specific_row

car_type = input('Enter car type, for example: Auta małe \n')
brand = input('Enter brand \n')
min_price = input('Enter minimal price \n')
max_price = input('Enter maximum price \n')
min_year = input('Enter minimum year \n')
max_year = input('Enter maximum year \n')
min_mileage = input('Enter minimum mileage \n')
max_mileage = input('Enter maximum mileage \n')
max_page = input('how many pages should be searched? \n')

create_database(DB_NAME=DB_NAME)
connect = connection(config=config)
cursor = connect.cursor()
create_table(cursor=cursor, TABLES=TABLES)

try:
    with Cars() as bot:
        correct_list = []
        bot.land_first_page()
        bot.accept_button()
        bot.car_type(car=car_type)
        bot.car_brand(brand=brand)
        bot.price(min_price=min_price, max_price=max_price)
        bot.years(min_year=min_year, max_year=max_year)
        bot.mileage(min_mileage=min_mileage, max_mileage=max_mileage)
        bot.search_all() 
        for page in range(1,max_page):
            data = bot.info()
            for row in data:
                correct_list.append( row)  
            if int(page) > 1:
                bot.page_change(page=page)
except:
    print('There is a problem with a main bot')


for row in correct_list:
    data_send(connect=connect, cursor=cursor, sql=add_new_row, data=row)

try:
    try:
        cursor.execute("SELECT title, city, price, year, mileage_km, engine_cm3, petrol from cars.car order by year asc limit 1")
        record = cursor.fetchall()
        first_ask = ''
        for row in record:
            first_ask = row
    except:
        print('Error with first table')
    try:
        cursor.execute("SELECT title, city, price, year, mileage_km, engine_cm3, petrol from cars.selected_car order by year asc limit 1")
        second_record = cursor.fetchall()
        second_ask = ''
        for row in second_record:
            if row != '' or row != None:
                second_ask =  row
    except:
        print('error with second table')
    try:
        if first_ask != second_ask:
            data_send(connect=connect, cursor=cursor, sql=add_specific_row, data=first_ask)
    except:
        print('Error with adding row to: cars.selected_car')
    try:
        cursor.execute("SELECT ID, title, city, price, year, mileage_km, engine_cm3, petrol from cars.selected_car order by year asc limit 1")
        second_record = cursor.fetchall()
        for data in second_record:
            message = 'title: {} \ncity: {} \nprice: {} \nyear: {} \nmileage: {} km2 \nengine: {} cm3 \npetrol: {}'.format(data[1],data[2],data[3],data[4],data[5],data[6],data[7])
            print(message)
            send_SMS(apikey='****API_KEY****', numbers='', author='', message=message)
    except:
        'Error with sms api'
except:
    print('Error with second part')

delete_database = input('Do you want delete database? Write Yes or Not \n')
if delete_database == 'yes' or delete_database == 'Yes' or delete_database == 'YES':
    try:    
        cursor.execute('DROP DATABASE cars')
        print('DATABASE WAS DELETED')
    except:
        print('Error with delete database')

cursor.close()
connect.close()

