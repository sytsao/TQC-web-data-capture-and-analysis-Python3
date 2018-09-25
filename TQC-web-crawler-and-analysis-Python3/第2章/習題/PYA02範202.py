import requests
import re

url = input('請填入要搜尋的網址：http://')
url='http://'+url
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    pattern = input("請輸入欲搜尋的字串 : ")    # pattern存放欲搜尋的字串

    if pattern in htmlfile.text:                
        print("搜尋 {:s} 成功".format(pattern))
    else:
        print("搜尋 {:s} 失敗".format(pattern))
  
    name = re.findall(pattern, htmlfile.text)  

    if name != None:
        print("{:s} 出現 {:d} 次".format(pattern, len(name)))
    else:
        print("{:s} 出現 0 次".format(pattern))
else:
    print("網頁下載失敗")
