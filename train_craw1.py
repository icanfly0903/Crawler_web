from selenium import webdriver
import time

PATH = "/usr/local/bin/chromedriver" # chromedriver address

driver = webdriver.Chrome(PATH) # open Chrome by chromedriver

driver.get("https://www.tiktok.com/?lang=vi-VN") # open a web by get https address

# print(driver.title) 

time.sleep(2) # do something after 2 seconds

element = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div/div[1]/a[1]')

element.click() # auto click

time.sleep(2)
# driver.quit()

element_username = driver.find_element_by_css_selector("h2.share-title")
element_fullname = driver.find_element_by_css_selector("h1.share-sub-title")
element_info = driver.find_element_by_css_selector("h2.share-desc")

print(element_username.text)
print(element_fullname.text)
print(element_info.text)