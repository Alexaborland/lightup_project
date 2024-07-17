import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium_project.base.base_class import Base
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class FindGroup(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Locators'''
    search_button = '//details-modal[@class="header__search"]'
    search_string = '//input[@class="search__input field__input"]'
    sort_price = '//details[@id="Details-1-template--15876164845825__main"]'
    price_from = '//input[@id="Filter-Price-GTE"]'
    price_to = '//input[@id="Filter-Price-LTE"]'
    availability = '//details[@id="Details-2-template--15876164845825__main"]'
    in_stock_checkbox = '//label[@for="Filter-Availability-1"]'
    sort_by = '//select[@id="SortBy"]'
    price_low_to_high = '//option[@value="price-ascending"]'
    product_1 = '//a[@class="full-unstyled-link"][1]'
    product_2 = '//a[@class="full-unstyled-link"][1]'
    cart = '//a[@id="cart-icon-bubble"]'

    '''Getters'''

    def get_search_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_search_string(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.search_string)))

    def get_filter_price_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.sort_price)))

    def get_price_from_string(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.price_from)))

    def get_price_to_string(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.price_to)))

    def get_availability(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.availability)))

    def get_in_stock_checkbox(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.in_stock_checkbox)))

    def get_sort_by(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.sort_by)))

    def get_price_low_to_high(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.price_low_to_high)))

    '''Actions'''

    def click_search_button(self):
        self.get_search_button().click()
        print('Clicked search button')

    def write_info_search_string(self, group_name):
        self.get_search_string().click()
        self.get_search_string().send_keys(group_name)
        print('Write down the group name')

    def submit_search(self):
        self.get_search_string().send_keys(Keys.ENTER)
        print('Pressed Enter to submit search')

    def click_filter_price_button(self):
        self.get_filter_price_button().click()
        print('Clicked filter price button')

    def write_price_from(self, first_price):
        self.get_price_from_string().send_keys(first_price)
        print('Write down the price FROM')

    def write_price_to(self, second_price):
        self.get_price_to_string().send_keys(second_price)
        print('Write down the price TO')

    def submit_price_range(self):
        self.get_price_to_string().send_keys(Keys.ENTER)
        self.get_price_to_string().send_keys(Keys.ESCAPE)
        print('Pressed Enter to submit price range')

    def click_availability_button(self):
        self.get_availability().click()
        print('Clicked availability button')

    def click_in_stock_checkbox(self):
        self.get_in_stock_checkbox().click()
        self.get_in_stock_checkbox().send_keys(Keys.ESCAPE)
        print('Clicked in stock checkbox')

    def click_sort_by(self):
        self.get_sort_by().click()
        print('Clicked sort by button')

    def click_price_low_to_high(self):
        self.get_price_low_to_high().click()
        print('Clicked sort by button')

    '''Methods'''

    def find_group_with_settings(self):
        self.get_current_url()
        self.click_search_button()
        self.write_info_search_string('Stray Kids')
        self.submit_search()
        self.click_filter_price_button()
        self.write_price_from('20')
        self.write_price_to('50')
        self.submit_price_range()
        time.sleep(1)
        self.click_availability_button()
        time.sleep(1)
        self.click_in_stock_checkbox()
        self.click_sort_by()
        time.sleep(3)
        self.click_price_low_to_high()
        time.sleep(3)


