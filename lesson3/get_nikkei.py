import requests
from bs4 import BeautifulSoup
import pandas as pd

page_init = 1
page_end = 3
Home_URL = "https://www.nikkei.com/"

titles = []
body_texts =[]
image_urls = []
for page in range(page_init, page_end + 1):
    Get_URL = "https://www.nikkei.com/business/net-media/?page=" + str(page)

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }

    nikkei_response = requests.get(Get_URL, headers=headers)
    soup = BeautifulSoup(nikkei_response.text, features="html.parser")
    links = soup.find_all("a", class_="fauxBlockLink_f6t5v6i")
    
    if page == 1:
        links_top = soup.find("a", class_="fauxBlockLink_f17mj100")
        links.insert(0, links_top)

    for link in links:
        try:
            titles.append(link.get_text().replace("\u3000", ""))
        except:
            pass

    body_links = []
    for link in links:
        try:
            body_links.append(link.get("href"))
        except:
            pass
    
    for body_link in body_links:
        get_body_link = Home_URL + body_link
        body_response = requests.get(get_body_link, headers=headers)
        body_soup = BeautifulSoup(body_response.text, features="html.parser")

        try:
            p_tag_text = body_soup.find("p", "paragraph_p18mfke4").get_text()
        except:
            pass
        body_texts.append(p_tag_text)

    image_class = "image_i1obkbgm"
    img_tags = soup.find_all("img", class_=image_class)
    
    for img_tag in img_tags:
        image_urls.append(img_tag.get("src"))

news_data = {
    "title": titles,
    "body_text": body_texts,
    "image_url": image_urls
    }

df = pd.DataFrame(news_data)
# df.to_csv("nikkei_news.csv", index=None, encoding="utf-8-sig")

for index, row in df.iterrows():
    get_image_url =  row["image_url"]
    filename = "img/" + str(index) + ".jpg"

    image = requests.get(get_image_url)
    with open(filename, "wb")as f:
        f.write(image.content)