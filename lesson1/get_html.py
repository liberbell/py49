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
print(imgage_tag1)
print(imgage_tags1)

imgage_tag2 = soup.find("img", id="size-small")
imgage_tags2 = soup.find_all("img", id="size-small")
print(imgage_tag2)
print(imgage_tags2)