import time

import pytest
from selenium_project.pages.find_product import FindGroup


def test_buy_product_1(set_up):
    driver = set_up
    print('Start test 1')
    login_page = FindGroup(driver)
    login_page.find_group_with_settings()

    time.sleep(3)
