import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://hosh-it.github.io/scraping-practice/"
response = requests.get(url)

# print(response.text)
soup = BeautifulSoup(response.text, features="html.parser")
# print(soup)

a_tags = soup.find_all("a")
print(a_tags)