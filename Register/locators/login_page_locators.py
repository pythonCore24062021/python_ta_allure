from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_EMAIL = (By.XPATH, '//*[@id="input-email"]')
    INPUT_PASSWORD = (By.XPATH, '//*[@id="input-password"]')
    ALERT_DIV = (By.XPATH, '/html/body/div[2]/div[1]')
    LOGIN_BTN = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
