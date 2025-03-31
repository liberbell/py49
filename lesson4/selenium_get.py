from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser
from time import sleep

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
driver.implicitly_wait(0.5)

driver.get(URL2)
username_element = driver.find_element(By.ID, "username")
password_element = driver.find_element(By.ID, "password")

username_element.send_keys(username)
password_element.send_keys(password)

login_element = driver.find_element(By.TAG_NAME, "button")
login_element.click()

# # driver.execute_script("return document.body.scrollHeight")
# driver.execute_script("return window.scrollTo(0, document.body.scrollHeight)")
# driver.save_screenshot("screen1.jpg")
# sleep(1)
# driver.execute_script("return window.scrollTo(0, document.body.scrollHeight)")
# driver.save_screenshot("screen2.jpg")
# sleep(1)
# driver.execute_script("return window.scrollTo(0, document.body.scrollHeight)")
# driver.save_screenshot("screen3.jpg")

content1 = driver.find_element(By.ID, "top-news-link")
print(content1.get_attribute("outerHTML"))
print(content1.get_attribute("href"))
print(content1.text)