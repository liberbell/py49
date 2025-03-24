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

all_text = []
img_urls = []
for get_url in a_tags_urls:
    sub_url = url + "/" + get_url
    sub_response = (requests.get(sub_url))
    sub_soup = BeautifulSoup(sub_response.text, features="html.parser")
    body_texts = sub_soup.find_all("p")
    img_tags = sub_soup.find_all("img")
    # print(img_tags)
    # print(body_texts)
    texts = ""
    
    for body_text in body_texts:
        texts += body_text.get_text()
        # print(body)
    # print("---P2---")
    all_text.append(texts)

    for img_tag in img_tags:
        img_urls.append(img_tag.get("src"))

web_data = {
    "title": a_tags_text,
    "url": a_tags_urls,
    "content": all_text,
    "image url": img_urls
}

df = pd.DataFrame(web_data)

for index, row in df.iterrows():
    img_url = row["image url"]
    get_img_url = url + "/" + img_url
    response_image = requests.get(get_img_url)


# for img_url in img_urls:
#     get_img_url = url + "/" + img_url
#     # print(get_img_url)
#     img_name = img_url[4:]
#     response_image = requests.get(get_img_url)
#     with open(img_name, "wb") as f:
#         f.write(response_image.content)
# print(df)
# df.to_csv("news_topic.csv", index=False)

