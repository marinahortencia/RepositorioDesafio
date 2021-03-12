import os
import datetime
import pyautogui
import pyscreeze
import time
from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.realpath(__file__)) + "/resources/chromedriver")
    #Browser manipulation
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

    with open("scenarios.txt", "a") as f:
        print(context.scenario.name, file=f)


def after_scenario(context, scenario):
    context.driver.close()
    
def after_step(context, scenario):
    name = context.scenario.name
    screenshot = pyautogui.screenshot()
    screenshot.save(name + datetime.datetime.now().strftime('%Y-%M-%d_%H%M%S'+'.png'))


def before_feature(context, feature):
    pass


def after_all(context):
    pass