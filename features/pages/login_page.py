from selenium.webdriver.common.by import By

class LoginPage:

    URL = 'https://www.saucedemo.com/'
    USERNAME_SELECTOR = (By.ID, 'user-name')
    PASSWORD_SELECTOR = (By.ID, 'password')
    LOGIN_BUTTON_SELECTOR = (By.ID, 'login-button')
    ERROR_MSG_SELECTOR = (By.XPATH, '//h3[@data-test="error"]')

    def __init__(self, browser):
        self.driver = browser.driver

    def get_page(self):
        self.driver.get(self.URL)

    def input_username(self, username):
        username_input = self.driver.find_element(*self.USERNAME_SELECTOR)
        username_input.send_keys(username)

    def input_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_SELECTOR)
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR)
        login_button.click()

    def get_error_message(self):
        error_message_box = self.driver.find_element(*self.ERROR_MSG_SELECTOR)
        return error_message_box.text