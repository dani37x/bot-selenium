DB_NAME = 'cars'

TABLES = {}

TABLES['car'] = (
    "CREATE TABLE `car`("
    "  `ID` int(11) NOT NULL AUTO_INCREMENT,"
    "  `title` varchar(100) NOT NULL,"
    "  `city` varchar(50) NOT NULL,"
    "  `price` int(10) NOT NULL,"
    "  `year` char(10) NOT NULL,"
    "  `mileage_km` int(10) NOT NULL,"
    "  `engine_cm3` int(10) NOT NULL,"
    "  `petrol` char(15) NOT NULL,"
    "  PRIMARY KEY (`ID`)"
    ") ENGINE=InnoDB")


TABLES['selected_car'] = (
    "CREATE TABLE `selected_car`("
    "  `ID` int(11) NOT NULL AUTO_INCREMENT,"
    "  `title` varchar(100) NOT NULL,"
    "  `city` varchar(50) NOT NULL,"
    "  `price` int(10) NOT NULL,"
    "  `year` char(10) NOT NULL,"
    "  `mileage_km` int(10) NOT NULL,"
    "  `engine_cm3` int(10) NOT NULL,"
    "  `petrol` char(15) NOT NULL,"
    "  PRIMARY KEY (`ID`)"
    ") ENGINE=InnoDB")



add_new_row = ("INSERT INTO car"
               "(title, city, price, year, mileage_km, engine_cm3, petrol)"
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")

add_specific_row = ("INSERT INTO selected_car"
               "(title, city, price, year, mileage_km, engine_cm3, petrol)"
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
