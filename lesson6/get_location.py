import configparser

config_ini = configparser.ConfigParser(interpolation=None)
config_ini.read('config.ini', encoding='utf-8')
get_url1 = config_ini['DEFAULT']['Get_URL1']

print(get_url1)