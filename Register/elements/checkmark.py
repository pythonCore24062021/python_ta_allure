from Register.elements.base import BaseElement
from Register.locators.register_page_locators import RegisterPageLocators




class PrivacyCheckmark(BaseElement):

    def __init__(self, driver, locators):
        super().__init__(driver, locators)
        self.checkbox = driver.find_element(*RegisterPageLocators.PRIVACYPOLICYCHECKMARK)

    def click(self):
        self.element.click()
        return self


