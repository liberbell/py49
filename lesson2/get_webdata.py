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
a_tags_urls = []
for a_tag in a_tags:
    a_tags_text.append(a_tag.get_text())
    a_tags_urls.append(a_tag.get("href"))

# print(a_tags_text)
# print(a_tags_urls)

for get_url in a_tags_urls:
    sub_url = url + "/" + get_url
    sub_response = requests.get(sub_url)
    # print(sub_response.text)

sub_soup = BeautifulSoup(sub_response, features="html.parser")
print(sub_soup)

# img_tags = soup.find_all("img")
# # print(img_tags)
# img_urls = []
# for img_tag in img_tags:
#     img_urls.append(img_tag.get("src"))
# print(img_urls)
