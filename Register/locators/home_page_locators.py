from selenium.webdriver.common.by import By


class HomePageLocators:
    MY_ACCOUNT_DROPDOWN = (By.XPATH, '//*[@id="top-links"]/ul/li[2]')
    REGISTER_LINK = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')
    LOGIN_LINK = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')