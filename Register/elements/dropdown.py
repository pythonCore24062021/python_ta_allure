
from Register.elements.base import BaseElement
# from Register.pages.login import Login
from Register.locators.home_page_locators import HomePageLocators
from Register.locators.register_page_locators import RegisterPageLocators
# from Register.pages.register_page import RegisterUser
from selenium.webdriver.common.keys import Keys


class Dropdown(BaseElement):
    def click(self):
        self.element.click()
    def select_by_value(self, value):
        self.driver.find_element_by_xpath(f""".//option[text()='{value}']""").click()




class DropdownRegionState(Dropdown):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)
        self.region_state = driver.find_element(*RegisterPageLocators.DROPDOWN_REGION_STATE)

    def select_first_value(self):
        self.region_state.click()
        self.region_state.send_keys(Keys.DOWN)
        self.region_state.send_keys(Keys.ENTER)
        return self
