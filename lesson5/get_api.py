import configparser
import requests
import pandas as pd

config_ini = configparser.ConfigParser(interpolation=None)
config_ini.read('config.ini', encoding='utf-8')
password = config_ini['DEFAULT']['password']
apikey = config_ini['DEFAULT']['apikey']

endpoints = "https://newsapi.org/v2/everything"

params = {}
params["apiKey"] = apikey
params["q"] = "HPE"
params["from"] = "2025-03-02"

response = requests.get(endpoints, params=params)
# print(response.text)

data = response.json()
import pprint
# pprint.pprint(data)
# print(len(data["articles"]))
# pprint.pprint(data["articles"][0])
article = data["articles"][0]["content"]
published = data["articles"][0]["publishedAt"]
title = data["articles"][0]["title"]

print(published, title)

news_data_list = []
for article in data["articles"]:
    news_data = [article["content"], article["publishedAt"], article["title"]]
    news_data_list.append(news_data)
