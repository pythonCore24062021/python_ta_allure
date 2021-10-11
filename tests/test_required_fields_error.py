import time
import unittest

from selenium import webdriver


from Register.pages.home import Home



class ErrorRegisterPage(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
        time.sleep(1)
        self.home = Home(self.driver_Error)

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_first_reg_user(self):
        register_page = self.home.get_header()\
            .account_dropdown\
            .click()\
            .clickRegister() \
            .click_continue()

        self.assertEqual(register_page.get_err_firstname().get_error(), 'First Name must be between 1 and 32 characters!')

    def test_required_fields_reg_user(self):
        register_page = self.home.get_header()\
            .account_dropdown\
            .click()\
            .clickRegister() \
            .click_continue()
        errors = register_page.get_errors_all_required_fields()
        self.assertEqual(len(errors), 9)
        self.assertEqual(errors[0].get_error(), "First Name must be between 1 and 32 characters!")
