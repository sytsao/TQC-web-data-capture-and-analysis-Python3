# coding: utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
driver_path = r"./chromedriver" # 改為你的 driver 路徑
driver = webdriver.Chrome(executable_path = driver_path)
# go to the google home page
driver.get("http://www.google.com")

# the page is ajaxy so the title is originally this:
print(driver.title)

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("q")

# type in the search
inputElement.send_keys("FIFA 2018")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()
time.sleep(3)
try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("FIFA 2018"))

    # You should see "cheese! - Google Search"
    print(driver.title)

finally:
    driver.quit()
