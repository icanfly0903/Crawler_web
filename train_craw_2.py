''''
#2: Web Scraping Filling Forms
'''

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

PATH = "/usr/local/bin/chromedriver" # chromedriver address

driver = webdriver.Chrome(PATH) # open Chrome by chromedriver

# driver.get("https://www.w3schools.com/html/html_forms.asp")

# time.sleep(2)

# input_fname = driver.find_element_by_id("fname") # get location to write 
# input_lname = driver.find_element_by_id("lname")

# input_fname.clear() # clear input 
# input_fname.send_keys("Vo") # give input a value
# time.sleep(2)
# input_lname.clear()
# input_lname.send_keys("Lam")
# time.sleep(2)
# input_lname.submit() # submit a web

driver.get("https://mdbootstrap.com/docs/b4/jquery/forms/select/")
time.sleep(2)

select_option = driver.find_element_by_css_selector("select.custom-select")
select_object = Select(select_option)

# Select an <option> based upon the <select> element's internal index
select_object.select_by_index(1)
time.sleep(2)

# Select an <option> based upon its value attribute
select_object.select_by_value('2')
time.sleep(2)

# Select an <option> based upon its text 
select_object.select_by_visible_text('Three')
time.sleep(2)
