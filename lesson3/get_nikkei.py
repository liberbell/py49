import requests
from bs4 import BeautifulSoup
import pandas as pd

Home_URL = "https://www.nikkei.com/business/net-media/"
nikkei_response = requests.get(Home_URL)
soup = BeautifulSoup(nikkei_response, features="html.parser")

print(soup)