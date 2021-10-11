import time


from Register.elements.button import Button
from Register.elements.input import Input
from Register.pages.base_page import BasePage
from Register.locators.login_page_locators import LoginPageLocators

class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = Input(driver, LoginPageLocators.INPUT_EMAIL)
        self.password_input = Input(driver, LoginPageLocators.INPUT_PASSWORD)
        self.login_btn = Button(driver, LoginPageLocators.LOGIN_BTN)

    def get_warning(self):
        self.warning = AlertDiv(self.driver, LoginPageLocators.ALERT_DIV)
        return self.warning

    def set_email(self, email):
        self.email_input.set_value(email)
        return self

    def set_password(self, email):
        self.password_input.set_value(email)
        return self
    def click_login(self):
        self.login_btn.click()
        time.sleep(2)
        try:
            self.get_warning()
            return self
        except:
            pass
