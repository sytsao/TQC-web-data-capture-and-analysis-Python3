import re
import urllib.request
import urllib.error
# 財政部官網
request_url = 'http://invoice.etax.nat.gov.tw/' 
def gethtmlfile(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    return html
htmlfile = gethtmlfile(request_url)
htmlcontent = htmlfile.read().decode('utf-8')
if htmlfile != None:
    pattern = input("請輸入欲搜尋的字串 : ")    # pattern存放欲搜尋的字串
    if pattern in htmlcontent:                
        print("搜尋 {:s} 成功".format(pattern))
    else:
        print("搜尋 {:s} 失敗".format(pattern))
  
    name = re.findall(pattern, htmlcontent)  

    if name != None:
        print("{:s} 出現 {:d} 次".format(pattern, len(name)))
    else:
        print("{:s} 出現 0 次".format(pattern))
else:
    print("網頁下載失敗")
