import requests
from bs4 import BeautifulSoup
import pandas as pd

page = 1
Home_URL = "https://www.nikkei.com/business/net-media/"
Get_URL = "https://www.nikkei.com/business/net-media/?page=" + str(page)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

nikkei_response = requests.get(Get_URL, headers=headers)
soup = BeautifulSoup(nikkei_response.text, features="html.parser")

# print(soup)

titles = soup.find_all("a", class_="fauxBlockLink_f6t5v6i")
title_top = soup.find("a", class_="fauxBlockLink_f17mj100")
titles.insert(0, title_top)
print(titles)