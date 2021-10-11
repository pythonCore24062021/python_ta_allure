import time
import unittest

import allure
from selenium import webdriver


from Register.pages.home import Home

@allure.description("""
RegisterPage
test firstName
""")
@allure.title("firs_name tests")
@allure.epic("epic_1")
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

    @allure.title("firs_name is long ")
    @allure.description("""
    firstName langs 33
    """)
    @allure.link('https://github.com/pythonCore24062021/TA/issues/8', name='Click me')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_first_reg_user(self):
        register_page = self.home.get_header()\
            .account_dropdown\
            .click()\
            .clickRegister().set_firstname("a"*33) \
            .click_continue()

        self.assertEqual(register_page.get_err_firstname().get_error(), 'First Name must be between 1 and 32 characters!')

    @allure.title("firs_name is long ")
    @allure.description("""
        firstName langs 33
        """)
    @allure.link('https://github.com/pythonCore24062021/TA/issues/8', name='Click me')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_first_reg_user(self):
        register_page = self.home.get_header() \
            .account_dropdown \
            .click() \
            .clickRegister().set_firstname("a" * 3) \
            .click_continue()

        self.assertEqual(register_page.get_err_firstname().get_error(),
                         'First Name must be between 1 and 32 characters!')

    @allure.link('https://github.com/pythonCore24062021/TA/issues/8')
    @allure.title("firs_name is empty")
    def test_required_fields_reg_user(self):
        register_page = self.home.get_header()\
            .account_dropdown\
            .click()\
            .clickRegister() \
            .click_continue()
        errors = register_page.get_errors_all_required_fields()
        self.assertEqual(len(errors), 9)
        self.assertEqual(errors[0].get_error(), "First Name must be between 1 and 32 characters!")
