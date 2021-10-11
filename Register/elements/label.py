from Register.elements.base import BaseElement



class Label(BaseElement):
    def get_label(self):
        return self.element.text

    