from features.browser import Browser
from features.pages.login_page import LoginPage
from features.pages.inventory import InventoryPage

def before_scenario(context, scenario):
    context.browser = Browser()
    context.login_page = LoginPage(context.browser)
    context.inventory_page = InventoryPage(context.browser)

def after_scenario(context, scenario):
    context.browser.quit()