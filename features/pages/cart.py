from selenium.webdriver.common.by import By
from features.pages.base import BasePage


class CartPage(BasePage):
    URL = 'https://www.saucedemo.com/cart.html'
    CART_TITLE_SELECTOR = (By.XPATH, '//span[@class="title"]')

    def get_cart_page_title(self):
        cart_title = self.driver.find_element(*self.CART_TITLE_SELECTOR)
        return cart_title.text
