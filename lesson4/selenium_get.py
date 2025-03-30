from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

username = config_ini['DEFAULT']['username']
password = config_ini['DEFAULT']['password']

URL1= "https://www.google.com"
URL2 = "https://hosh-it.github.io/scraping-practice-selenium/"

def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    return options

options = get_default_chrome_options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get(URL2)
username_element = driver.find_element(By.ID, "username")
password_element = driver.find_element(By.ID, "password")

username.send_keys("hoshi")
password.send_keys("pass")