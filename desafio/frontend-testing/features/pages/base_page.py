from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def refresh(self):
        self.driver.refresh()


    def open_url(self, url):
        self.driver.get(url)
    

    def get_url(self, url):
        self.open_url(url)


    def get_title(self):
        return self.driver.title


    def click(self, locator, seconds = 10):
        self.wait_for(EC.element_to_be_clickable(locator), seconds).click()


    def click_generic(self, ec, seconds = 10):
        self.wait_for(ec, seconds=seconds).click()


    def click_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()


    def find(self, locator, seconds=20):
        element = self.wait_for(EC.visibility_of_element_located(locator), seconds)
        return element


    def find_condition(self, condition, seconds = 10):
        element = self.wait_for(condition, seconds=seconds)
        return element


    def find_is_presence(self, locator, seconds = 10):
        element = self.wait_for(EC.presence_of_element_located(locator), seconds)
        return element


    def find_elements(self, locator, seconds = 10):
        element = self.wait_for(EC.visibility_of_all_elements_located(locator), seconds)
        return element

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def elements_by_name(self, locator):
        return self.driver.find_elements_by_name(locator)


    def elements_by_class(self, locator):
        return self.driver.find_elements_by_class_name(locator)


    def wait_for(self, condition, seconds = 10):
        return  WebDriverWait(self.driver, seconds).until(condition)
        

    def type_in(self, locator, text, set_clear=True, set_enter=False, click=False):
        element = self.find(locator)
        if set_clear:
            self.clear_input_text(locator)
        if click:
            self.click(locator)
        if set_enter:
            element.send_keys(text, Keys.ENTER)
        else:
            element.send_keys(text)
        

    def type_in_is_presence(self, locator, text, set_clear=True, set_enter=False):
        element= self.find_is_presence(locator)
        if set_clear:
            element.clear()
        if set_enter:
            element.send_keys(text, Keys.ENTER)
        else:
            element.send_keys(text)


    def type_in_condition(self,condition,text,set_clear = True, set_enter = False):
        element= self.find_condition(condition)
        if set_clear:
            element.clear()
        if set_enter:
            element.send_keys(text, Keys.ENTER)
        else:
            element.send_keys(text)


    def wait(self, time):
        WebDriverWait(self.driver, time)


    def type_with_javascript_by_class_name(self, class_name, index, text):
        self.driver.execute_script('document.getElementsByClassName("' + class_name + '")[' + index + '].innerHTML = "' + text + '";')


    def select_in_combo_visible_text(self, locator, value):
        Select(self.wait_for(EC.visibility_of_element_located(locator))).select_by_visible_text(value)


    # def select_in_combo_by_value(self, locator, value):
    #    Select(self.wait_for(EC.visibility_of_element_located(locator))).select_by_value(value)
    
    
    def find_by_id(self, id):
        return self.driver.find_element_by_id(id)


    def press_down(self, locator):
        self.find(locator).send_keys(Keys.ARROW_DOWN)


    def press_enter(self, locator):
        self.find(locator).send_keys(Keys.RETURN)


    def press_space_bar(self, locator, index=0):
        if index == 0:
            self.find(locator).send_keys(Keys.SPACE)
        else:
            self.find_elements(locator)[index].send_keys(Keys.SPACE)
    

    def press_back_space(self, locator, index=0):
        if index == 0:
            self.find(locator).send_keys(Keys.BACK_SPACE)
        else:
            self.find_elements(locator)[index].send_keys(Keys.BACK_SPACE)


    def pause(self, seconds = 1):
        ActionChains(self.driver).pause(seconds).perform()


    def move_to_element(self, locator):
        element = self.find_is_presence(locator)
        ActionChains(self.driver).move_to_element(element).perform()


    def element_is_displayed(self, locator, seconds = 10):
        try:
            element = self.find(locator, seconds)
            if element == None:
                return False
            else:
                return True
        except TimeoutException:
            return False


    def press_ctrl(self, locator, button):
        self.find(locator).send_keys(Keys.CONTROL + button)


    def press_delete(self, locator):
        self.find(locator).send_keys(Keys.DELETE)


    def is_display(self, locator, seconds = 10):
        return self.find(locator, seconds).is_displayed()
    

    def is_not_displayed(self, locator, seconds = 10):
        visible = True
        time = 1
        while ( visible == True and time <= seconds):
            self.pause()
            time = time + 1
            try:
                visible = self.is_display(locator, 2)
            except:
                visible = False


    def is_enabled(self, locator):
        return self.find(locator).is_enabled()


    def is_present_in_grid(self, value):                                        
        for colum in self.driver.find_elements_by_css_selector("div[class$='itemNotLast___1d4Dd']"):
            if colum.text == value:
                return True
        return False


    def java_script_executor(self, script):
        return self.driver.execute_script(script)


    def clear_input(self, locator, index=0):
        if index == 0:
            self.find(locator).clear()
        else:
            self.find_elements(locator)[index].clear


    def verify_exist_elements(self, ec):                                        
        control = True
        try:
            if self.find_condition(ec, seconds=2):
                control = True
        except :
            control = False
        return control


    def clear_input_text(self, locator):
        element = self.find(locator)
        text = element.get_attribute('value')
        text_length = len(text)
        while text_length > 0:
            self.type_in(locator, Keys.BACK_SPACE, set_clear=False)
            text_length = text_length - 1
