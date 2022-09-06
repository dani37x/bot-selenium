from lib2to3.pgen2.token import OP
from project_files import Operations
import mysql.connector
from mysql.connector import errorcode

def value(price, data_type):
    price = price.split(data_type)[0]
    price = price.replace(" ", "")
    price = int(price)
    return price


def try_connect(config):
    try:
        connect = Operations(config=config)
        return connect
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)