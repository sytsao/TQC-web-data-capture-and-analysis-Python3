# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import datetime
today = str(datetime.date.today())
cwb_data = "cwb_weather_data"
import urllib.request
import zipfile 
res ="http://opendata.cwb.gov.tw/opendataapi?dataid=F-D0047-093&authorizationkey=CWB-3FB0188A-5506-41BE-B42A-3785B42C3823"
urllib.request.urlretrieve(res,"F-D0047-093.zip")
f=zipfile.ZipFile('F-D0047-093.zip')
file = ['63_72hr_CH.xml']
CITY = []
DISTRICT = []
GEOCODE = []
DAY = []
TIME = []
T = []
Wx = []
for filename in file:
    try:
        data = f.read(filename).decode('utf8')
        soup = BeautifulSoup(data,"xml")
        city = soup.locationsName.text
        a = soup.find_all("location")
        for i in range(0,len(a)):
            location = a[i]
            district = location.find_all("locationName")[0].text
            geocode = location.geocode.text
            weather = location.find_all("weatherElement")
            time = weather[1].find_all("dataTime")
            for j in range(0,len(time)):
                x = time[j].text.split("T")
                DAY.append(x[0])
                time_1 = x[1].split("+")
                TIME.append(time_1[0])
                CITY.append(city)
                DISTRICT.append(district)
                GEOCODE.append(geocode)
            for t  in weather[0].find_all("value"):
                T.append(t.text)
            wx = weather[9].find_all("value")
            for w in range(0,len(wx),2):
                Wx.append(wx[w].text)
    except:
        break
f.close()
data = {"CITY":CITY,"DISTRICT":DISTRICT,"GEOCODE":GEOCODE,"DAY" : DAY,"TIME" : TIME,"T":T,"Wx": Wx}
df = pd.DataFrame(data,columns=["CITY","DISTRICT","GEOCODE","DAY","TIME","T","Wx"])
save_name = "taiwan_cwb" + today + ".csv"
df.to_csv(save_name,index=False,encoding="utf_8_sig")
