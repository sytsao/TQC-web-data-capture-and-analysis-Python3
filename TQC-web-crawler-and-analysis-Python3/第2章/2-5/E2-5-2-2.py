# coding: utf-8
# # 動態網頁擷取
# ## Yahoo! 奇摩股市：上市單日成交價排行
# 
# - 前往 Yahoo! 奇摩股市
# - 點選**更多排行**
# - 點選**上市行情類排行榜：單日成交價排行**
# - 點選**列出前一百名排行**
# - 將股票代號/名稱擷取下來
from selenium import webdriver  
driver_path = r"./chromedriver" # 改為你的 driver 路徑
driver = webdriver.Chrome(executable_path = driver_path)
driver.get("https://tw.finance.yahoo.com/")
more_rank_elem = driver.find_element_by_css_selector('.yui-text-left .yui-text-left table tr:nth-child(1) .stext div a')
more_rank_elem.click()
price_rank_elem = driver.find_element_by_css_selector('.yui-text-left+ .yui-text-left tr:nth-child(5) a')
price_rank_elem.click()
top_100_elem = driver.find_element_by_css_selector('p a+ a')
top_100_elem.click()
ticker_name_elem = driver.find_elements_by_css_selector('.name')
ticker_name = [tn.text for tn in ticker_name_elem]
driver.close()
print(ticker_name)
