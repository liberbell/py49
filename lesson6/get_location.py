import configparser
import requests
from bs4 import BeautifulSoup
from lxml import html

config_ini = configparser.ConfigParser(interpolation=None)
config_ini.read('config.ini', encoding='utf-8')
get_url1 = config_ini['DEFAULT']['Get_URL1']

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
response = requests.get(get_url1, headers=headers)

soup = BeautifulSoup(response.text, features="html.parser")
lxml_data = html.fromstring(str(soup))

get_bus_no = lxml_data.xpath("//table/tbody/tr/td/text()")
# print(get_bus_no)

get_bus_time = lxml_data.xpath("//div/div/p/strong/text()")
# /html/body/section/div[3]/div/div[1]/div/div/p[1]/strong
print(get_bus_time)