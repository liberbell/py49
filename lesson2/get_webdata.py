import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://hosh-it.github.io/scraping-practice/"
response = requests.get(url)

# print(response.text)
soup = BeautifulSoup(response.text, features="html.parser")
# print(soup)

a_tags = soup.find_all("a")
# print(a_tags)
a_tags_text = []
for a_tag in a_tags:
    a_tags_text.append(a_tag.get_text())

# print(a_tags_text)

img_tags = soup.find("img")
print(img_tags)
img_urls = []
for img_tag in img_tags:
    img_urls.append(img_tags.get("src"))
print(img_urls)
