from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from features.pages.base import BasePage


class InventoryPage(BasePage):

    URL = 'https://www.saucedemo.com/inventory.html'
    TITLE_SELECTOR = (By.CLASS_NAME, 'title')
    PRODUCTS_SELECTOR = (By.CLASS_NAME, 'inventory_item')
    ADD_TO_CART_SELECTOR = (By.ID, "add-to-cart-sauce-labs-onesie")
    REMOVE_FROM_CART_SELECTOR = (By.ID, "remove-sauce-labs-onesie")
    CART_BADGE_SELECTOR = (By.XPATH, '//span[@class="shopping_cart_badge"]')

    def get_page_title(self):
        title_element = self.driver.find_element(*self.TITLE_SELECTOR)
        return title_element.text

    def get_products_count(self):
        products = self.driver.find_elements(*self.PRODUCTS_SELECTOR)
        return len(products)

    def add_product_to_cart(self):
        add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_SELECTOR)
        add_to_cart_button.click()

    def remove_button_exists(self):
        try:
            self.driver.find_element(*self.REMOVE_FROM_CART_SELECTOR)
            return True
        except NoSuchElementException:
            return False

    def get_cart_badge_counter(self):
        cart_badge_counter = self.driver.find_element(*self.CART_BADGE_SELECTOR)
        return cart_badge_counter.text
