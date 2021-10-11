from Register.elements.base import BaseElement


class Link(BaseElement):
    def click(self):
        self.element.click()
