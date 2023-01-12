from behave import *

@Given("I am on the Sign in page")
def step_impl(context):
    context.login_page.get_page()

@When('I input a "{username}" username')
def step_impl(context, username):
    context.login_page.input_username(username)

@When('I input a "{password}" password')
def step_impl(context, password):
    context.login_page.input_password(password)

@When("I click the login button")
def step_impl(context):
    context.login_page.click_login()

@Then("I receive the Epic sadface error message")
def step_impl(context):
    expected_err_msg = 'Epic sadface: Username and password do not match any user in this service'
    assert context.login_page.get_error_message() == expected_err_msg

@Then("I am on the Inventory page")
def step_impl(context):
    #1. Ne asiguram ca avem URL-ul corect
    assert context.browser.get_current_url() == context.inventory_page.URL

    #2. Verificam ca avem titlul corect in pagina
    assert context.inventory_page.get_page_title() == 'PRODUCTS'
