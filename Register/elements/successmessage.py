from Register.elements.base import BaseElement



class Message(BaseElement):
    def get_message(self):
        return self.element.text

