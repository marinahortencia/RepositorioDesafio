from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class LoginPage(BasePage):
    email = (By.ID, "email")
    password = (By.ID, "passwd")
    login_button = (By.ID, "SubmitLogin")
    
    def set_email(self, email):
        sleep(1)
        super().type_in(self.email, email)
        sleep(1)
    
    def set_password(self, password):
        sleep(1)
        super().type_in(self.password, password)
        sleep(1)

    def click_login_button(self):
        sleep(1)
        super().click(self.login_button)
        sleep(2)