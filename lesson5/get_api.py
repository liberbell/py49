import configparser
import requests

config_ini = configparser.ConfigParser(interpolation=None)
config_ini.read('config.ini', encoding='utf-8')
password = config_ini['DEFAULT']['password']
apikey = config_ini['DEFAULT']['apikey']

endpoints = "https://newsapi.org/v2/everything"

params = {}
params["apiKey"] = apikey
params["q"] = "HPE"
params["from"] = "2025-03-01"

response = requests.get(endpoints, params=params)
print(response.text)