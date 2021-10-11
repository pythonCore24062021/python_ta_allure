from Register.elements.base import BaseElement
from selenium.webdriver.support.color import Color


class Color(BaseElement):
    def get_text_color(self, find_element_by_class_name=None):
        rgb = find_element_by_class_name("col-sm-2 control-label").value_of_css_property('color')
        self.driver.rgb.text()
        hex = Color.from_string(rgb).hex
        return hex

