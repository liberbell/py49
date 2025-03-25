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

a_tags = soup.find_all("a")
print(a_tags)