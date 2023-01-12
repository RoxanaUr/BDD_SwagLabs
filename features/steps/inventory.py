from behave import *


@When('I login successfully with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)


@Then("There are 6 product on the Inventory page")
def step_impl(context):
    assert context.inventory_page.get_products_count() == 6


@Given('I am not a logged in user')
def step_impl(context):
    pass


@When('I try to access the Inventory page')
def step_impl(context):
    context.inventory_page.get_page()


@Then('I am redirected to Login page')
def step_impl(context):
    assert context.browser.get_current_url() == context.login_page.URL


@Then('I receive a Epic sadface error message')
def step_impl(context):
    expected_error_message = "Epic sadface: You can only access '/inventory.html' when you are logged in."
    assert context.login_page.get_error_message() == expected_error_message
