'''
#3: ActionChains Automation
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "/usr/local/bin/chromedriver" # chromedriver address

driver = webdriver.Chrome(PATH) # open Chrome by chromedriver

'''
Drag & Drop Action
driver.get("http://www.essemble.co.uk/escript/drag_drop_engine/dragdrop1.html")
time.sleep(6)

for i in range(1, 9):
    source_element = driver.find_element_by_id(f"drag{i}")

    target_element = driver.find_element_by_id(f"drop{i}")

    action = ActionChains(driver)
    action.drag_and_drop(source_element, target_element)
    action.pause(1) # pasue 1 second
    action.perform() # perform all stored action

time.sleep(2)
btn_confirm = driver.find_element_by_id("btn")
btn_confirm.click()
'''

driver.get("http://scraper.dev/test/1.html")
time.sleep(2)

div_tittle = driver.find_element_by_tag_name("div")

action = ActionChains(driver)
action.double_click(div_tittle)
action.pause(1)

for i in range(20):
    action.double_click(div_tittle)
    action.pause(1)

action.perform()