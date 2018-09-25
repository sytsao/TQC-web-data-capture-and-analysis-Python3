# coding: utf-8
import requests
from bs4 import BeautifulSoup
url = "https://www.youtube.com/results?search_query=fifa+2018"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")

for all_mv in soup.select(".yt-lockup-video"):
    # 抓取 Title & Link
    data = all_mv.select("a[rel='spf-prefetch']")
    print("名稱: {}".format(data[0].get("title")))
    print("連結: https://www.youtube.com{}".format(data[0].get("href")))
    # 抓取觀看時間與人數
    data = all_mv.select(".yt-lockup-meta-info")
    time = data[0].get_text("#").split("#")[0]
    see = data[0].get_text("#").split("#")[1]
    print("發佈時間: {}".format(time))
    print("觀看人數: {}".format(see))
    # 抓取Img
    data = all_mv.select("a[rel='spf-prefetch']")
    img = all_mv.select("img")
    if img[0].get("src") != "/yts/img/pixel-vfl3z5WfW.gif":
        print("照片: {}".format(img[0].get("src")))
    else:
        print("照片: {}".format(img[0].get("data-thumb")))
    print("-------------------")

