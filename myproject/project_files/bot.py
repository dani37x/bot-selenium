from project_files import link as url
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from project_files import value
import time



class Cars(webdriver.Chrome):
    def __init__(self, driver_path='D:\projekty\bot\chromedriver',
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Cars, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(url.URL)

    def accept_button(self):
        accept = self.find_element(By.ID,
            'onetrust-accept-btn-handler'
        )
        accept.click()
    
    def car_type(self, car=None):
        self.implicitly_wait(10)
        car_list = self.find_element(By.XPATH,
           '//input[@placeholder="Typ nadwozia"]'
        )
        car_list.send_keys(car)
        car_list.send_keys(Keys.ENTER)
    
    def car_brand(self, brand=None):
        self.implicitly_wait(15)
        brand_list = self.find_element(By.XPATH,
            '//input[@placeholder="Marka pojazdu"]'                               
        )
        brand_list.send_keys(brand)
        accept = self.find_element(By.XPATH,
            '//ul[@class="ooa-126x4ro"]/li[2]'
        )
        accept.click()

    def car_model(self, model=None):
        self.implicitly_wait(15)
        model_list = self.find_element(By.XPATH,
            '//input[@placeholder="Model pojazdu"]'                               
        )
        model_list.send_keys(model)
        accept = self.find_element(By.XPATH,
            '//ul[@class="ooa-126x4ro"]/li[1]'
        )
        accept.click()        

    def car_generation(self, generation=None):
        self.implicitly_wait(15)
        generation_list = self.find_element(By.XPATH,
            '//input[@placeholder="Generacja"]'                               
        )
        generation_list.send_keys(generation)
        accept = self.find_element(By.XPATH,
            '//ul[@class="ooa-126x4ro"]/li[1]'
        )
        accept.click()  
        
    def price(self, min_price, max_price):
        if min_price != '':
            self.implicitly_wait(2)
            minimum = self.find_element(By.XPATH,
                '//input[@placeholder="od"]'                             
            )
            minimum.send_keys(min_price)
            accept = self.find_element(By.XPATH,
                '//ul[@class="ooa-126x4ro"]/li[1]'
            )
            accept.click()  
        if max_price != '':
            self.implicitly_wait(2)
            maximum = self.find_element(By.XPATH,
                '//input[@placeholder="do"]'                             
            )
            maximum.send_keys(max_price)
            accept = self.find_element(By.XPATH,
                '//ul[@class="ooa-126x4ro"]/li[1]'
            )
            accept.click()  
        
    def years(self, min_year, max_year):
        if min_year != '':
            self.implicitly_wait(2)
            minimum = self.find_element(By.XPATH,
                '//input[@id="filter_float_year:from"]'                             
            )
            minimum.send_keys(min_year)
            accept = self.find_element(By.XPATH,
                '//ul[@class="ooa-126x4ro"]/li[1]'
            )
            accept.click()  
        if max_year != '':
            self.implicitly_wait(2)
            maximum = self.find_element(By.XPATH,
                '//input[@id="filter_float_year:to"]'                             
            )
            maximum.send_keys(max_year)
            accept = self.find_element(By.XPATH,
                '//ul[@class="ooa-126x4ro"]/li[1]'
            )
            accept.click()  
        
    def mileage(self, min_mileage, max_mileage):
        if min_mileage != '':
            self.implicitly_wait(5)
            minimum = self.find_element(By.XPATH,
                '//input[@id="filter_float_mileage:from"]'                             
            )
            minimum.send_keys(min_mileage)
            accept = self.find_element(By.XPATH,
                '//ul[@class="ooa-126x4ro"]/li[1]'
            )
            accept.click()  
        if max_mileage != '':
            self.implicitly_wait(5)
            maximum = self.find_element(By.XPATH,
                '//input[@id="filter_float_mileage:to"]'                             
            )
            maximum.send_keys(max_mileage)
            accept = self.find_element(By.XPATH,
                '//ul[@class="ooa-126x4ro"]/li[1]'
            )
            accept.click()  
    
    def search_all(self):
        self.implicitly_wait(10)
        button = self.find_element(By.CSS_SELECTOR,
            '[data-testid="submit-btn"]'                           
        )
        # second option
        button = self.find_element(By.XPATH,
            '//*[@data-testid="submit-btn"]'                       
        )
        self.implicitly_wait(20)
        time.sleep(15)
        button.click()
    
    
    def info(self):
        self.implicitly_wait(60)
        titles = self.find_elements(By.XPATH,
           '//h2[@data-testid="ad-title"]'
        )
        cities = self.find_elements(By.XPATH,
            "//p[@class='e1b25f6f6 ooa-1otyv8u-Text eu5v0x0']"
        )
        prices = self.find_elements(By.XPATH,
            "//span[@class='ooa-epvm6 e1b25f6f7']"
        )
        years = self.find_elements(By.XPATH,
            "//ul[@class='e1b25f6f6 ooa-ggoml6-Text eu5v0x0']/li[1]"
        )
        mileages = self.find_elements(By.XPATH,
            "//ul[@class='e1b25f6f6 ooa-ggoml6-Text eu5v0x0']/li[2]"
        )
        engines = self.find_elements(By.XPATH,
            "//ul[@class='e1b25f6f6 ooa-ggoml6-Text eu5v0x0']/li[3]"
        )
        petrols = self.find_elements(By.XPATH,
            "//ul[@class='e1b25f6f6 ooa-ggoml6-Text eu5v0x0']/li[4]"
        )
        info_list = []                
        for  title, city, price, year, mileage, engine, petrol in zip(titles, cities, prices, years, mileages, engines, petrols):
            price = value(price=price.text, data_type='PLN')    
            mileage = value(price=mileage.text, data_type='km')      
            engine = value(price=engine.text, data_type='cm3')
            # print(title.text, city.text, price, year.text, mileage, engine, petrol.text)      
            info_list.append([title.text, city.text, price, year.text, mileage, engine, petrol.text])
        return info_list       


    def page_change(self, page=None):
        self.implicitly_wait(60)
        # print(self.current_url)
        next_page = str(self.current_url) + '&page=' + str(page)
        self.get(next_page)

