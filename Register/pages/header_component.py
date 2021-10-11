from Register.elements.dropdown import Dropdown
from Register.locators.home_page_locators import HomePageLocators


class DropdownMyAccount(Dropdown):

    def __init__(self, driver, locators):
        super().__init__(driver, locators)
        self.register = driver.find_element(*HomePageLocators.REGISTER_LINK)
        self.login = self.driver.find_element(*HomePageLocators.LOGIN_LINK)

    def click(self):
        self.element.click()
        return self

    def clickLogin(self):
        self.login.click()
        from Register.pages.login import Login
        return Login(self.driver)

    def clickRegister(self):
        self.register.click()
        from Register.pages.register_page import RegisterUser
        return RegisterUser(self.driver)


class HeaderComponent:
    def __init__(self, driver):
        self.driver = driver
        self.account_dropdown = DropdownMyAccount(self.driver, HomePageLocators.MY_ACCOUNT_DROPDOWN)
