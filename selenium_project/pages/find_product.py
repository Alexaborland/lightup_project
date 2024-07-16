from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium_project.base.base_class import Base
from selenium.webdriver.common.keys import Keys


class FindGroup(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Locators'''
    search_button = '//svg[@class="modal__toggle-open icon icon-search"]'
    search_string = '//input[@class="search__input field__input"]'
    sort_price = '//details[@id="Details-1-template--15876164845825__main"]'
    price_from = '//input[@id="Filter-Price-GTE"]'
    price_to = '//input[@id="Filter-Price-LTE"]'
    availability = '//details[@id="Details-2-template--15876164845825__main"]'
    in_stock_checkbox = '//input[@id="Filter-Availability-1"]'
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

    '''Actions'''

    def click_search_button(self):
        self.get_search_button().click()
        print('Clicked search button')

    def put_info_search_string(self, group_name):
        self.get_search_string().click()
        self.get_search_string().send_keys(group_name)
        print('Write down the group name')

    def submit_search(self):
        self.get_search_string().send_keys(Keys.ENTER)
        print('Pressed Enter to submit search')

    '''Methods'''

    def input_information(self):
        self.get_current_url()
        self.click_search_button()
        self.put_info_search_string('Stray Kids')
        self.submit_search()


