DB_NAME = 'cars'

TABLE = {}

TABLE['employees'] = (
    "CREATE TABLE `car` ("
    "  `ID` int(11) NOT NULL AUTO_INCREMENT,"
    "  `title` varchar(50) NOT NULL,"
    "  `city` varchar(20) NOT NULL,"
    "  `price` int(10) NOT NULL,"
    "  `year` int(10) NOT NULL,"
    "  `mileage_km` int(10) NOT NULL,"
    "  `engine_cm3` int(10) NOT NULL,"
    "  `petrol` char(15) NOT NULL,"
    "  PRIMARY KEY (`ID`)"
    ") ENGINE=InnoDB")