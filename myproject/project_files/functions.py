import mysql.connector
from mysql.connector import errorcode
from project_files.config import conn
import urllib.request
import urllib.parse

def value(price, data_type):
    price = price.split(data_type)[0]
    price = price.replace(" ", "")
    price = int(price)
    return price


def connection(config):
    try:
        connect = mysql.connector.connect(**config)
        if connect:
            return connect
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
 

def create_database( DB_NAME):
    try:
        connect = mysql.connector.connect(**conn)
        cursor = connect.cursor()
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {} ".format(err))


def create_table(cursor, TABLES):
    for table_name in TABLES:
        # print('table name::: ',table_name)
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
    else:
        print("OK")


def data_send(connect, cursor, sql, data):
    cursor.execute( sql, data)
    connect.commit()

def send_SMS(apikey, *numbers, author, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'author': author})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.txtlocal.com/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)


def optional_price(price):
    values = [2000, 3000, 5000, 10000, 15000, 20000,
    25000, 30000, 35000, 40000, 50000, 65000, 80000,
    100000, 200000, 500000, 1000000, 7500000]
    if price in values:
        return True
    else:
        return False

def optional_year(year):
    years = [i for i in range(1992,2023)]
    if year in years:
        return True
    else:
        return False

# def optional_petrol(petrol):
#     petrols = ['Benzyna', 'Benzyna+CNG', 'Benzynza+LPG',
#     'Diesel', 'Elektryczny', 'Etanol', 'Hybryda', 'Wodór']
#     if petrol in petrols:
#         return True
#     else:
#         return False

def optional_mileage(mileage):
    mileages = [20000, 30000, 35000, 50000,
    75000, 100000, 125000, 200000, 250000]
    if mileage in mileages:
        return True
    else:
        return False

def change_format(value):
    number = str(value)
    number = [number[i:i+3] for i in range(0, len(number), 3)]
    number = ' '.join([number[i:i+3] for i in range(0, len(number), 3)])
    print(number)
    return number





