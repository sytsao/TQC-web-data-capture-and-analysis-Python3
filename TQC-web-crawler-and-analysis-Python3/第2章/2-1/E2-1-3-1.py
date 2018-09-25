#抓取粉絲專頁資訊-貼文/讚數/分享數
import requests
import pandas as pd 
from dateutil.parser import parse
token = 'EAAdRZAEpt638BAGCQZC9co68ndjyxgHrLoScGjXtxZBept6YOlAZAuT4jgKv50EzrHAI8mG3l8ZBPNVK3ypE8on9e3byrtvsDZCir9FQaLOZAAkUQiPZAkZBddhtmVn4GVd8ZB7kZBQieUpnSF9HkIh1GVrtM3M4ynZC38TWM1LvfSejiUiJxUEIZAJ5je8M4ydOjU3NGFjsP2Hv96AZDZD'
fanpage_id = '145649977189'
res = requests.get('https://graph.facebook.com/v3.0/{}/posts?limit=100&access_token={}'.format(fanpage_id, token))
posts = []
page = 1
while 'paging' in res.json():
    print('目前正在抓取第%d頁' % page)
    for post in res.json()['data']:
        res2 = requests.get('https://graph.facebook.com/v2.8/{}?fields=likes.limit(0).summary(True), shares&access_token={}'.format(post['id'], token))
        if 'likes' in res2.json():
            likes = res2.json()['likes']['summary'].get('total_count')
        else:
            likes = 0
        if 'shares' in res2.json():
            shares = res2.json()['shares'].get('count')
        else:
            shares = 0
        posts.append([parse(post['created_time']),  post['id'], post.get('message'), post.get('story'), likes, shares])
    if 'next' in res.json()['paging']:
        res = requests.get(res.json()['paging']['next'])
        page += 1
    else:
        break
print('抓取結束!')
df = pd.DataFrame(posts)
df.columns = ['貼文時間', '貼文ID', '貼文內容', '分享內容', '讚數', '分享數']
df.to_csv('E2-1-3-1-output.csv', index=False)