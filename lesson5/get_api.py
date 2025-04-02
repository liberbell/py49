import configparser

config_ini = configparser.ConfigParser(interpolation=None)
config_ini.read('config.ini', encoding='utf-8')
password = config_ini['DEFAULT']['password']
apikey = config_ini['DEFAULT']['apikey']

print(apikey, password)

endpoints = "https://newsapi.org/v2/everything"