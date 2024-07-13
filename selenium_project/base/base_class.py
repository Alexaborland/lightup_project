import os
import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    '''Method get current url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    '''Method assert word'''

    def checking_word(self, checking_word, checking_result):
        value_word = checking_word.text
        assert value_word == checking_result
        print('The word is same')

    '''Method screenshot'''
    def get_screenshot(self):
        base_dir = 'C:\\Users\\HP\\PycharmProjects\\stepik_main_project\\selenium_project'
        sub_dir = 'screen\\'
        full_path = os.path.join(base_dir, sub_dir)

        now_date = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot(full_path + name_screenshot)

    '''Method assert url'''
    def assert_url(self, result_url):
        get_url = self.driver.current_url
        assert get_url == result_url
        print('Get value url')
