# -*- coding: utf-8 -*-
import bs4, requests

url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)

objSoup = bs4.BeautifulSoup(html.text, 'lxml')     


dataTag = objSoup.select('.contents_box02')        

balls = dataTag[2].find_all('div', {'class':'ball_tx ball_yellow'})
print("大樂透開獎 : ", end='')
print()
print('-------------')
print("開出順序 : ", end='')
for i in range(6):                                  
    print(balls[i].text, end='   ')

print("\n大小順序 : ", end='')
for i in range(6,len(balls)):                      
    print(balls[i].text, end='   ')


                
redball = dataTag[2].find_all('div', {'class':'ball_red'})
print("\n特別號   :", redball[0].text)




