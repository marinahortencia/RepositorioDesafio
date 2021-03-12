import os
import sys
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from pages.base_page import BasePage
from time import sleep

@step(u'I enter on main url')
def step_impl(context):
    BasePage(context.driver).get_url("http://automationpractice.com/")