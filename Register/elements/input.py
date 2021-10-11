import allure

from Register.elements.base import BaseElement
from selenium.webdriver.common.keys import Keys



class Input(BaseElement):
    def click(self):
        self.element.click()

    @allure.step("set input value {text}")
    def set_value(self, text):
        self.element.clear()
        self.element.send_keys(text)

    def get_value(self):
        return self.element.text()

    def press_enter(self):
        self.element.send_keys(Keys.ENTER)

