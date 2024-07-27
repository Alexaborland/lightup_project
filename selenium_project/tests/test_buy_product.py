import time

import pytest
from selenium_project.pages.find_product_with_settings import Add_Product_To_Cart


def test_buy_product_1(set_up):
    driver = set_up
    print('Start test 1')
    find_the_group = Add_Product_To_Cart(driver)
    find_the_group.add_product_to_cart_with_settings()
    time.sleep(3)



