#-*-coding:utf-8-*-

import pdfkit
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
import requests
from bs4 import BeautifulSoup

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""

res = requests.get('http://news.sina.com.cn/c/nd/2017-09-09/doc-ifykusey6584342.shtml')
soup = BeautifulSoup(res.content,'html.parser')
article = soup.select('.article.article_16')[0]
article = str(article)
html = html_template.format(content = article)
html = html.encode('utf-8')

with open('GE1-8-out.html','wb') as f:
    f.write(html)

pdfkit.from_file('GE1-8-out.html','GE1-8-out.pdf',configuration=config)
print('succeed')