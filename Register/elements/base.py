
from selenium.webdriver.support.color import Color
class BaseElement:
    def __init__(self, driver, locators=None, element=None):
        self.driver = driver
        self.locator = locators
        self.element = self.driver.find_element(*self.locator) if element is None else element

    def get_color_hex(self):
        return Color.from_string(self.element.value_of_css_property("color")).hex

