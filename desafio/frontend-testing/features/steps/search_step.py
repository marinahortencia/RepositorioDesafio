import os
import sys
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from hamcrest import assert_that, equal_to
from pages.search_page import SearchPage
from time import sleep

@step(u'I am on search screen')
def step_impl(context):
    context.page_object = SearchPage(context.driver)
    
@then(u'I verify the search title "{title}"')
def step_impl(context, title):
    assert_that(context.page_object.get_search_title_page(), equal_to(title))
    
@then(u'I verify that the returned search is correct "{text}"')
def step_impl(context, title):
    assert_that(context.page_object.get_text_searched(), equal_to(text))
    
@then(u'I verify that result number is correct "{value}"')
def step_impl(context, value):
    assert_that(context.page_object.get_number_result_search(), equal_to(value))
    
@then(u'I verify that product name is equal to searched "{product_name}"')
def step_impl(context, product_name):
    assert_that(context.page_object.get_product_name(), equal_to(product_name))
    
@step(u'I click on product details')
def step_impl(context):
    context.page_object.click_details_view()
    
@then(u'I verify the product condition is equal to displayed "{condition}"')
def step_impl(context, condition):
    assert_that(context.page_object.get_condition(), equal_to(condition))
    
@then(u'I verify that the product description is "{description}"')
def step_impl(context, description):
    assert_that(context.page_object.get_description(), equal_to(description))
    
       
    