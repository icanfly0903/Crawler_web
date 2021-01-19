from selenium import webdriver
import time

PATH = "/usr/local/bin/chromedriver" # chromedriver address

driver = webdriver.Chrome(PATH) # open Chrome by chromedriver

driver.get("https://www.google.com/") # open a web by get https address

print(driver.title) 

time.sleep(2) # close the web after 2 second

driver.quit()