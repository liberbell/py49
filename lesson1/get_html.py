import requests
from bs4 import BeautifulSoup

url = "https://hosh-it.github.io/scraping-practice/"
response = requests.get(url=url)

# print(response.status_code)
# print(response.text)

soup = BeautifulSoup(response.text)
print(soup.prettify())