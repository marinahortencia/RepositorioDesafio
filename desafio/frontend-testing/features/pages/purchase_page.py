from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.select import Select


class PurchasePage(BasePage):
    add_cart_button = (By.ID, "add_to_cart")
    message_added_cart = (By.XPATH, "//span[@class='cross']/following-sibling::h2[1]")
    proceed_checkout_cart_button = (By.XPATH, "//a[@title='Proceed to checkout']//span[1]")
    proceed_checkout_sumary = (By.XPATH, "(//a[@title='Proceed to checkout']//span)[2]")
    proceed_checkout_address = (By.XPATH, "//span[text()='Proceed to checkout']")
    proceed_checkout_shipping =  (By.XPATH, '//*[@id="form"]/p/button')
    payment_check = (By.XPATH, "//a[@title='Pay by check.']")                                      
    agree_message = (By.XPATH, '//*[@id="form"]/div/p[2]/label')
    confirm_order_button = (By.XPATH, "(//button[@type='submit']//span)[2]")
    message_order_successfuly = (By.XPATH, '//*[@id="center_column"]/p[1]/text()')
    
    
    def get_message_added_cart_successfuly(self):
        sleep(2)
        return super().find_element(self.message_added_cart).text
        sleep(2)
    
    def click_add_to_cart(self):
        sleep(2)
        super().click(self.add_cart_button)
        sleep(2)
        
    def click_proceed_checkout_cart_button(self):
        sleep(2)
        super().click(self.proceed_checkout_cart_button)
        sleep(2)
        
    def click_proceed_checkout_sumary(self):
        sleep(2)
        super().click(self.proceed_checkout_sumary)
        sleep(2)
        
    def click_proceed_checkout_address(self):
        sleep(2)
        super().click(self.proceed_checkout_address)
        sleep(2)
        
    def click_proceed_checkout_shipping(self):
        sleep(2)
        super().click(self.proceed_checkout_shipping)
        sleep(2)
        
    def click_agree_check_box(self):
        sleep(2)
        super().click(self.agree_message)
        sleep(2)
        
    def get_message_agree_terms(self):
        sleep(2)
        return super().find_element(self.agree_message).text
        sleep(2)
        
    def click_payment_check(self):
        sleep(2)
        return super().find_element(self.payment_check)
        sleep(2)
        
    def click_confirm_order_button(self):
        sleep(2)
        return super().find_element(self.confirm_order_button)
        sleep(2)
        
    def get_message_order_successfuly(self):
        sleep(3)
        return super().find_element(self.message_order_successfuly).text
        sleep(3)
        