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

links = soup.find_all("a", class_="fauxBlockLink_f6t5v6i")
links_top = soup.find("a", class_="fauxBlockLink_f17mj100")
links.insert(0, links_top)
# print(links)

titles = []
for link in links:
    titles.append(link.get_text().replace("\u3000", ""))

# print(titles)

body_links = []
for link in links:
    body_links.append(link.get("href"))

print(body_links)