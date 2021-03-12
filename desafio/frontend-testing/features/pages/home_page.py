from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class HomePage(BasePage):
    login_option = (By.ID, "span-loginInvitationText")
    cart_option = (By.XPATH, "//div[@class='shopping_cart']//a")
    search_field = (By.ID, "search_query_top")
    search_button = (By.NAME, "submit_search")
    sign_option = (By.CLASS_NAME, "login")
    
    
    def set_search_text(self, text):
        super().type_in(self.search_field, text)
        sleep(2)
    
    def click_search_button(self):
        sleep(2)
        super().click(self.search_button)
        sleep(3)
    
    def click_cart_option(self):
        super().click(self.cart_option)
        
    def click_sign_button(self):
        sleep(1)
        super().click(self.sign_option)
        sleep(1)