# -*- coding: utf-8 -*-
import os
import sys
from bs4 import BeautifulSoup
from selenium import webdriver  

# 參數定義
path_PhantomJS    = os.getcwd()+"./phantomjs.exe"
scraping_url      = "https://www.paymentscardsandmobile.com/uks-tesco-tests-checkout-free-shopping/"
# 啟動 WebDriver (背景執行的 PhantomJS)
browser = webdriver.PhantomJS(executable_path = path_PhantomJS)
browser.get(scraping_url)
# 如果網站在 10 秒內回應則繼續執行下一步，否則等待 10 秒
browser.implicitly_wait(10)
new_result = []
# 取得網頁原始碼並交由 BeautifulSoup 進行解析
html_soup = BeautifulSoup(browser.page_source, "lxml")
new_title    = html_soup.find("h1", attrs={"itemprop": "name"}).get_text().strip(' \t\n\r\xa0')
new_date     = html_soup.find("div", attrs={"class": "post-meta cf"}).find("time", attrs={"itemprop": "datePublished"})['title']
new_contents = []
for content in html_soup.find("div", attrs={"itemprop": "articleBody"}).find_all("p"):
    c = ""
    try:
        # 過濾掉圖例說明的內容
        if not content['class']:
            c = content.get_text().strip(' \t\n\r\xa0')
    except KeyError:
        c = content.get_text().strip(' \t\n\r\xa0')
    if len(c) > 0:
        # 將 ISO/IEC_8859-1 代表空白的 &nbsp (non-breaking space) 取代為標準的空白字元(\x20)
        c = c.replace('\xa0', ' ')
        new_contents.append(c)
# 列印處理結果
print("Final Result:")
print("News url: {}".format(scraping_url))
print("News title: {}".format(new_title))
print("News date: {}".format(new_date))
print("Content:")
for n in new_contents:
    print(print(str("{}\n".format(n)).encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)))
browser.close() 