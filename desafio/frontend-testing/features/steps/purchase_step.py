import os
import sys
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from pages.purchase_page import PurchasePage
from hamcrest import assert_that, equal_to

@step(u'I am on Purchase screen')
def step_impl(context):
    context.page_object = PurchasePage(context.driver)

@step(u'I click on add to cart button')
def step_impl(context):
    context.page_object.click_add_to_cart()
    
@then(u'I verify the the product is added "{message}"')
def step_impl(context, message):
    assert_that(context.page_object.get_message_added_cart_successfuly(), equal_to(message))
    
@step(u'I click on proceed checkout cart button')
def step_impl(context):
    context.page_object.click_proceed_checkout_cart_button()
    
@step(u'I click on proceed checkout sumary button')
def step_impl(context):
    context.page_object.click_proceed_checkout_sumary()
    
@step(u'I click on proceed checkout shipping button')
def step_impl(context):
    context.page_object.click_proceed_checkout_shipping()
    
@step(u'I click on proceed checkout address button')
def step_impl(context):
    context.page_object.click_proceed_checkout_address()
    
@then(u'I verify the term message to agree "{message}"')
def step_impl(context, message):
    assert_that(context.page_object.get_message_agree_terms(), equal_to(message))
    
@step(u'I click on agree checkbox')
def step_impl(context):
    context.page_object.click_agree_check_box()
    
@step(u'I click on payment check option')
def step_impl(context):
    context.page_object.click_payment_check()
    
@step(u'I click confirm order')
def step_impl(context):
    context.page_object.click_confirm_order_button()
    
@then(u'I verify that the order is finish "{message}"')
def step_impl(context, message):
    assert_that(context.page_object.get_message_order_successfuly(), equal_to(message))
    
