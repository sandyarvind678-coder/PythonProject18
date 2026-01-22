from behave import given, when, then
from cucumberpages.loginpage import LoginPage

@given("user opens the login page")
def step_open_login(context):
    context.page.goto("https://example.com/login")
    context.login = LoginPage(context.page)

@when("user enters username and password")
def step_enter_credentials(context):
    context.login.enter_username()
    context.login.enter_password()
    context.login.click_login()

@then("user should be logged in")
def step_verify_login(context):
    context.page.wait_for_timeout(3000)
