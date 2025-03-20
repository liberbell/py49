import requests
from bs4 import BeautifulSoup

url1 = "https://hosh-it.github.io/scraping-practice/"
url2 = "https://hosh-it.github.io/scraping-practice/practice.html"
response = requests.get(url=url2)

# print(response.status_code)
# print(response.text)

soup = BeautifulSoup(response.text, features="html.parser")
# print(soup.prettify())

image_tags = soup.find_all("img")

imgage_tag1 = soup.find("img", class_="size-middle")
imgage_tags1 = soup.find_all("img", class_="size-middle")
# print(imgage_tag1)
# print(imgage_tags1)

imgage_tag2 = soup.find("img", id="small-size")
imgage_tags2 = soup.find_all("img", id="small-size")
# print(imgage_tag2)
# print(imgage_tags2)

# print(imgage_tag2.get("src"))

# for i in image_tags:
#     # print(i)
#     print(i["src"])

print("------")
image_src_list = []
for image in image_tags:
    image_src_list.append(image.get("src"))

print(image_src_list)

print("------")

a_tags = soup.find_all("a")
print(a_tags)
href_list = []
a_text_list = []
for href in a_tags:
    href_list.append(href.get("href"))
    a_text_list.append(href.get_text())

print(href_list)
print(a_text_list)