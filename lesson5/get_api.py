import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
apikey = config_ini['DEFAULT']['apikey']
password = config_ini['DEFAULT']['password']
print(apikey, password)

endpoints = "https://newsapi.org/v2/everything"