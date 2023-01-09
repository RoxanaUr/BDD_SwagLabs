from features.browser import Browser
from features.pages.login_page import LoginPage

def before_scenario(context, scenario):
    context.browser = Browser()
    context.login_page = LoginPage(context.browser)


def after_scenario(context, scenario):
    context.browser.quit()