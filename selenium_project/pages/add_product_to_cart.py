import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium_project.base.base_class import Base
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class AddProductToCart(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Locators'''
    product_link = '(//div[@class="card-wrapper underline-links-hover"])[1]'

    '''Getters'''

    def get_product_link(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.product_link)))

    '''Actions'''

    def click_on_the_product(self):
        self.get_product_link().click()
        print('Clicked on the product')

    '''Methods'''

    def add_the_product_to_cart(self):
        self.click_on_the_product()
        time.sleep(3)
