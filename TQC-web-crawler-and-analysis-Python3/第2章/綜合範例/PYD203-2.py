# -*- coding: utf-8 -*-
from selenium import webdriver
import csv
import time

chromedriver = r"./chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
csvr_site = csv.reader(open('site.csv', 'r',encoding='utf-8'))
csvr_terms = csv.reader(open('terms.csv', 'r',encoding='utf-8'))
outfile = open('rank.csv', 'w',encoding='utf-8')
csvwriter = csv.writer(outfile)
search_pages = 10

for s in csvr_site:
    site = s[0]
 
for row in csvr_terms:
    current_page = 1
    while current_page < search_pages:
        if current_page == 1:
            driver.get("https://www.google.com.tw/search?q=%s" % row[0])
        else:
            driver.get(next_pageurl)
        time.sleep(1)
        doms = driver.find_elements_by_css_selector("div.rc h3.r a")
        next_pageurl = driver.find_element_by_css_selector("a#pnnext.pn").get_attribute("href")
        counter = 0
        rank = "not found"
        for dom in doms:
            counter += 1   
            href = dom.get_attribute("href")
            if site in href:
                rank = counter
                break
        if rank != "not found":
            break
        current_page += 1
 
    csvwriter.writerow([row[0], current_page, rank])
    outfile.flush()
    time.sleep(1)
driver.close()
