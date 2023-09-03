# coupang selenium 4.12

from selenium import webdriver

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.18 Safari/537.36"


driver = webdriver.Chrome()

url = "https://www.coupang.com/vp/products/131222787?itemId=386242196"
driver.get(url)
print(driver.page_source)




