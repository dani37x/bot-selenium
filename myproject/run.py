from project_files import Cars
# from project_files import Operations
from project_files import try_connect
from project_files import config


try:
    cursor = try_connect(config=config)
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
            data = bot.info()

            for row in data:
                print(row)

            if int(page) > 1:
                bot.page_change(page=page)   
except:
    'There is a problem with a main bot'
