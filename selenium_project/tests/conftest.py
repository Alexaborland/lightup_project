import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function', autouse=True)
def set_up():
    print('\nStart test')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    url = 'https://lightupk.com/'
    driver.get(url)
    driver.maximize_window()

    yield driver

    # driver.quit()
    print('\nFinish test')


@pytest.fixture(scope='module', autouse=True)
def set_group():
    print('\nEnter system')
    yield
    print('\nExit system')
