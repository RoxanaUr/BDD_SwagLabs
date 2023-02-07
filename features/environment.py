from features.browser import Browser
from features.pages.login_page import LoginPage
from features.pages.inventory import InventoryPage
from features.pages.cart import CartPage

def before_scenario(context, scenario):
    context.browser = Browser()
    context.login_page = LoginPage(context.browser)
    context.inventory_page = InventoryPage(context.browser)
    context.cart_page = CartPage(context.browser)

def after_scenario(context, scenario):
    context.browser.quit()