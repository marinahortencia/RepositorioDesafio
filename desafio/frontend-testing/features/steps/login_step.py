import os
import sys
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from pages.login_page import LoginPage
from hamcrest import assert_that, equal_to

@step(u'I am on login screen')
def step_impl(context):
    context.page_object = LoginPage(context.driver)

@step(u'I type the email "{email}"')
def step_impl(context, email):
    context.page_object.set_email(email)
    
@step(u'I type the password "{password}"')
def step_impl(context, password):
    context.page_object.set_password(password)

@step(u'I click on login button')
def step_impl(context):
    context.page_object.click_login_button()
