from Register.elements.base import BaseElement


class Error(BaseElement):
    def get_error(self):
        return self.element.text