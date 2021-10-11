import time
import unittest

import allure
from selenium import webdriver

import sys
print(sys.path)

from Register.pages.home import Home


class RegisterPage(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
        time.sleep(1)
        self.home = Home(self.driver)

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @allure.description("""
    test firstname error color.
    """)
    @allure.epic("epic_1")
    @allure.story('story_1')
    def test_color_required_fields(self):
        register_page = self.home.get_header()\
            .account_dropdown\
            .click()\
            .clickRegister() \
            .click_continue()
        firstname_label = register_page.get_firstname_label()

        self.assertEqual(firstname_label.get_color_hex(), '#a94442')
