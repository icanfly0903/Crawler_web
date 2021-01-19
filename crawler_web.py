from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

name = "xiaomi"

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
images = []
products = []  # List to store name of the product
prices = []  # List to store price of the product
reviews = []
driver.get(f"https://tiki.vn/search?q={name}&ref=searchBar")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll("a", href=True, attrs={"class": "product-item"}):
    name = a.find("div", attrs={"class": "name"})
    price = a.find("div", attrs={"class": "price-discount__price"})
    review = a.find("div", attrs={"class": "review"})

    if review == None:
        continue
    else:
        reviews.append(review.text)
        
    products.append(name.text)
    prices.append(price.text)

df = pd.DataFrame({"Product Name": products, "Price": prices, "Review": reviews})
df.to_csv("products.csv", index=False, encoding="utf-8")
