import os
import sys
from pages.base_page import BasePage
from pages.home_page import HomePage
from time import sleep
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)


@step(u'I am on home screen')
def step_impl(context):
    context.page_object = HomePage(context.driver)

@step(u'I type the search text "{text}"')
def step_impl(context, text):
    context.page_object.set_search_text(text)
       
@step(u'I click on search button')
def step_impl(context):
    context.page_object.click_search_button()
    
@step(u'I click on sign')
def step_impl(context):
    context.page_object.click_sign_button()