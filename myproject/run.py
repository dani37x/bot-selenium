from project_files import Cars
from project_files import Operations
from project_files import config
from project_files import connection, create_database, create_table
from project_files.query import DB_NAME, TABLES

connect = connection(config=config)
cursor = connect.cursor()
create_database(cursor=cursor, DB_NAME=DB_NAME)
create_table(cursor=cursor, TABLES=TABLES)
cursor.close()
connect.close()
# cursor.execute("SHOW TABLES")

# for x in cursor:
#   print(x)

# try:
#     with Cars() as bot:
#         bot.land_first_page()
#         bot.accept_button()
#         bot.car_type(car='Auta małe')
#         bot.car_brand(brand='Renault')
#         bot.price(min_price='0', max_price='15000')
#         bot.years(min_year='2000', max_year='2010')
#         bot.mileage(min_mileage='0', max_mileage='2000000')
#         bot.search_all()
#         for page in range(1,5):
#             data = bot.info()

#             for row in data:
#                 print(row)

#             if int(page) > 1:
#                 bot.page_change(page=page)   
# except:
#     'There is a problem with a main bot'
