from project_files import link as url
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os




class Cars(webdriver.Chrome):
    def __init__(self, driver_path='D:\projekty\bot\chromedriver',
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Cars, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()


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
        brand_list.send_keys(Keys.ENTER)
        
    def price(self, min_price, max_price):
        self.implicitly_wait(2)
        minimum = self.find_element(By.XPATH,
            '//input[@id="filter_float_price:from"]'                             
        )
        minimum.send_keys(min_price)
        minimum.send_keys(Keys.ENTER)
        
        self.implicitly_wait(2)
        maximum = self.find_element(By.XPATH,
            '//input[@id="filter_float_price:to"]'                             
        )
        maximum.send_keys(max_price)
        maximum.send_keys(Keys.ENTER)
        
    def years(self, min_year, max_year):
        self.implicitly_wait(2)
        minimum = self.find_element(By.XPATH,
            '//input[@id="filter_float_year:from"]'                             
        )
        minimum.send_keys(min_year)
        minimum.send_keys(Keys.ENTER)
        
        self.implicitly_wait(2)
        maximum = self.find_element(By.XPATH,
            '//input[@id="filter_float_year:to"]'                             
        )
        maximum.send_keys(max_year)
        maximum.send_keys(Keys.ENTER)
        
    def mileage(self, min_mileage, max_mileage):
        self.implicitly_wait(2)
        minimum = self.find_element(By.XPATH,
            '//input[@id="filter_float_mileage:from"]'                             
        )
        minimum.send_keys(min_mileage)
        minimum.send_keys(Keys.ENTER)
        
        self.implicitly_wait(2)
        maximum = self.find_element(By.XPATH,
            '//input[@id="filter_float_mileage:to"]'                             
        )
        maximum.send_keys(max_mileage)
        maximum.send_keys(Keys.ENTER)
    
    def search_all(self):
        self.implicitly_wait(10)
        button = self.find_element(By.CSS_SELECTOR,
            '[data-testid="submit-btn"]'                           
        )
        # second option
        button = self.find_element(By.XPATH,
            '//*[@data-testid="submit-btn"]'                       
        )
        self.implicitly_wait(10)
        button.click()
    
    def city(self):
        self.implicitly_wait(30)
        elements = self.find_elements(By.XPATH,
            '//p[@class="e1b25f6f7 ooa-1otyv8u-Text eu5v0x0"]'                
        )
        for element in elements:
            print( element.text)
       

    def info_car(self):
        self.implicitly_wait(30)
        elements = self.find_elements(by="xpath",
            value='//article[@class="ooa-1sz58zb e1b25f6f18"]'            
        )
        for element in elements:
            title = element.find_element(by="xpath", value='./div/h2/a').text
            print(title)
            year = element.find_element(by="xpath", value="./div/div/ul/li[1]").text
            print(year)
            distance = element.find_element(by="xpath", value="./div/div/ul/li[2]").text
            print(distance)
            engine = element.find_element(by="xpath", value="./div/div/ul/li[3]").text
            print(engine)
            petrol = element.find_element(by="xpath", value="./div/div/ul/li[4]").text
            print(petrol)
            
            
    # def pages(self, page):
    #     self.implicitly_wait(60)
    #     self.page = page
    #     # //*[name()='svg' and @class="ooa-1xwoou1"]
    #     # next_page = self.find_element(By.PARTIAL_LINK_TEXT,
    #     #     f'{self.page}'
    #     # )
    #     next_page = self.find_element(By.XPATH,
    #         '//*[name()="svg" and @class="ooa-1xwoou1"]'
    #     )
    #     next_page.click()
    #     print('loooool')