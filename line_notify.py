from bs4 import BeautifulSoup
import requests
import random
import time
import re
import json
import pandas as pd
import numpy as np


my_token = "7YoFcw3smG1t4SHZkD4A9WzCVjuqJDg5nxyPppz4Re2"
ptt_articles_path = './data/articles.csv'

tracked_list = ['stock', 'cfp']
url_list = ["https://www.ptt.cc/bbs/Stock/index.html", "https://www.ptt.cc/bbs/cfp/index.html"]
# url = "https://www.ptt.cc/man/part-time/DF76/D780/DC4F/index.html"

data = pd.read_csv(ptt_articles_path)
print(data)
big_bros = ['drgon', 'TccReD', 'zesonpso', 'YingLinga', 'hong888', 'test520', 'newconfidenc', 'weekend88123',]

headers = {
    "Authorization": "Bearer " + my_token,
    "Content-Type": "application/x-www-form-urlencoded"
}

cnt = 1
while True:

    for i in range(len(url_list)):

        url = url_list[i]
        panel = tracked_list[i]

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("div", class_="r-ent")

        # if cnt == 1:
        #     r = requests.post("https://notify-api.line.me/api/notify",
        #     headers=headers, params={'message': "本報告目前追蹤PTT股票板以下高手文章:{}".format(big_bros)})

        for _ in articles:
            meta = _.find("div", class_='meta')
            title = _.find("div", class_='title').text.strip()
            author = meta.find(class_='author').text.strip()
            date = meta.find(class_='date').text.strip()


            if author in big_bros:
                
                ### 文章網址
                article_a = _.select('div.title > a')
                article_a = str(article_a).split('"')
                article_url = 'https://www.ptt.cc' + article_a[1]
                
                # print('Date:', date)
                # print('Title: ', title)
                # print('Author: ', author)
                # print('url: ', article_url)

                exist = sum(data['url'].isin([article_url]))

                if exist:
                    print('作者{}這篇已經在{}板發過鮭魚報告了!'.format(author, panel))
                else:
                    print('作者{}這篇尚未在{}板發過，現在建立鮭魚報告。'.format(author, panel))
                    new_series = pd.Series([date, author, article_url], index=['date','author','url'])
                    data = data.append(new_series, ignore_index=True)
                    data.to_csv(ptt_articles_path, index=False)
                
                    params = {"message": "鮭魚快報:{}在ptt {}板發文了!\n{}".format(author, panel, article_url)}

                    r = requests.post("https://notify-api.line.me/api/notify",
                                    headers=headers, params=params)
                    print(r.status_code)  #200
    
    print('Iteration {}:'.format(cnt), time.ctime())
    cnt += 1
    time.sleep(120 + random.random()*10-5)
    