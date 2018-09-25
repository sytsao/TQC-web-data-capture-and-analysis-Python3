# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver_path = r"./chromedriver" # 改為你的 driver 路徑
driver = webdriver.Chrome(executable_path = driver_path)
driver.get("http://www.python.org")
print(driver.title)
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print(driver.page_source)
driver.close()
