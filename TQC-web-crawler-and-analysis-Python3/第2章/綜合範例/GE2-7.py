# -*- coding: utf-8 -*-
import os
import sys
from bs4 import BeautifulSoup
from selenium import webdriver  

path_PhantomJS    = os.getcwd()+"./phantomjs.exe"
scraping_url      = "http://www.paymentscardsandmobile.com/"
# 啟動 WebDriver (背景執行的 PhantomJS)
browser = webdriver.PhantomJS(executable_path = path_PhantomJS)
browser.get(scraping_url)
browser.maximize_window()
# 如果網站在 10 秒內回應則繼續執行下一步，否則等待 10 秒
browser.implicitly_wait(10)
new_result = []
# 取得網頁原始碼並交由 BeautifulSoup 進行解析
html_soup = BeautifulSoup(browser.page_source, "lxml")
# 找出所有的單篇新聞區塊
for tag_article in html_soup.find("div", attrs={"class": "posts-list listing-alt"}).find_all("article"):
    date    = tag_article.find("time", attrs={"itemprop": "datePublished"}).get_text().strip(' \t\n\r')
    url     = tag_article.find("a", attrs={"itemprop": "name url"})['href']
    title   = tag_article.find("a", attrs={"itemprop": "name url"}).get_text().strip(' \t\n\r')
    content = tag_article.find("p").get_text().strip(' \t\n\r')
    new_result.append([date, url, title, content])
print(str(new_result).encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
browser.close()