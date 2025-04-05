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

get_bus_nos = lxml_data.xpath("//tbody/tr[1]/td/text()")
# print(get_bus_nos)

get_bus_times = lxml_data.xpath("//div/div/p[1]/strong/text()")
# /html/body/section/div[3]/div/div[1]/div/div/p[1]/strong
# /html/body/section/div[6]/div/div[1]/div/div/p[1]/strong
# print(get_bus_times)
bus_nums = []
for get_bus_no in get_bus_nos:
    bus_num_list = [char for char in get_bus_no if char.isalnum()]
    bus_num = "".join(bus_num_list)
    bus_nums.append(bus_num)

bus_times = []
for get_bus_time in get_bus_times:
    bus_time_list = [char for char in get_bus_time if char.isalnum()]
    bus_time = "".join(bus_time_list)
    bus_times.append(bus_time)

# print(len(bus_times))
bus_time_len = len(bus_times)
bus_time_text = []
for i in range(bus_time_len):
    if bus_times[0] == "児童公園前に":
        bus_time_text.append(bus_times[i] + bus_times[i + 1] + bus_times[i + 2])
        i += 1

print(bus_time_text)


# print(bus_nums)