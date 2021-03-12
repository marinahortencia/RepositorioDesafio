from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.select import Select


class SearchPage(BasePage):
    text_searched = (By.CLASS_NAME, "lighter")
    number_result_search = (By.CLASS_NAME, "heading-counter")
    product_name = (By.XPATH, "(//a[@title='Faded Short Sleeve T-shirts'])[2]")
    details_view = (By.LINK_TEXT, "Faded Short Sleeve T-shirts")
    price = (By.CLASS_NAME, "our_price_display")
    condition =  (By.XPATH, "//span[text()='New']")
    description = (By.ID, "short_description_content")
    
    
    def get_search_title_page(self):
        sleep(2)
        return super().find_element(self.search_title_page).text
        sleep(2)

    def get_text_searched(self):
        sleep(2)
        return super().find_element(self.text_searched).text
        sleep(2)
    
    def get_number_result_search(self):
        sleep(2)
        return super().find_element(self.number_result_search).text
        sleep(2)
        
    def get_product_name(self):
        sleep(2)
        return super().find_element(self.product_name).text
        sleep(2)
        
    def click_details_view(self):
        sleep(2)
        super().click(self.details_view)
        sleep(2)
        
    def get_condition(self):
        sleep(2)
        return super().find_element(self.condition).text
        sleep(2)
        
    def get_description(self):
        sleep(2)
        return super().find_element(self.description).text
        sleep(2)
    