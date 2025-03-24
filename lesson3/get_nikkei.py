import requests
from bs4 import BeautifulSoup
import pandas as pd

Home_URL = "https://www.nikkei.com/business/net-media/"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

nikkei_response = requests.get(Home_URL, headers=headers)
soup = BeautifulSoup(nikkei_response.text, features="html.parser")

print(soup)