import requests

url = "https://hosh-it.github.io/scraping-practice/"
response = requests.get(url=url)

print(response.status_code)