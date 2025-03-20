import requests
from bs4 import BeautifulSoup

url1 = "https://hosh-it.github.io/scraping-practice/"
url2 = "https://hosh-it.github.io/scraping-practice/practice.html"
response = requests.get(url=url2)

# print(response.status_code)
# print(response.text)

soup = BeautifulSoup(response.text, features="html.parser")
# print(soup.prettify())

print(soup.find("img"))