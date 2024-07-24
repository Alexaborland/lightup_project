import time

import pytest
from selenium_project.pages.find_product_with_settings import FindGroup
from selenium_project.pages.add_product_to_cart import AddProductToCart


def test_buy_product_1(set_up):
    driver = set_up
    print('Start test 1')
    find_the_group = FindGroup(driver)
    find_the_group.find_group_with_settings()
    time.sleep(3)

    add_to_cart = AddProductToCart(driver)
    add_to_cart.add_the_product_to_cart()


