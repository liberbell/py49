import configparser
import requests
from bs4 import BeautifulSoup

config_ini = configparser.ConfigParser(interpolation=None)
config_ini.read('config.ini', encoding='utf-8')
get_url1 = config_ini['DEFAULT']['Get_URL1']

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
response = requests.get(get_url1, headers=headers)

soup = BeautifulSoup(response.text, features="html.parser")
print(soup)