from project_files.bot import Cars
import time

try:
    with Cars() as bot:
        bot.land_first_page()
        bot.accept_button()
        bot.car_type(car='Auta małe')
        bot.car_brand(brand='Renault')
        bot.price(min_price='0', max_price='15000')
        bot.years(min_year='2000', max_year='2010')
        bot.mileage(min_mileage='0', max_mileage='2000000')
        bot.search_all()
        for page in range(1,5):
            bot.info()
            if int(page) > 1:
                bot.page_change(page=page)
            print('PAGE::::::::',int(page))
        print('after')
        
except:
    'There is a problem with a main bot'
