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
    options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    return options

options = get_default_chrome_options()

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
# print(content1.get_attribute("outerHTML"))
# print(content1.get_attribute("href"))
# print(content1.text)
content1_url = content1.get_attribute("href")

# content1_data = webdriver.Chrome(options=options)
# content1_data.implicitly_wait(0.5)
# content1_data.get(content1_url)

# content1_ps = content1_data.find_elements(By.TAG_NAME, "p")
# for content1_p in content1_ps:
#     print(content1_p.text)

# contents = driver.find_elements(By.CLASS_NAME, "sub-article-link")
# for content in contents:
#     print(content.get_attribute("outerHTML"))
#     print(content.get_attribute("href"))
#     print(content.text)

height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("return window.scrollTo(0, document.body.scrollHeight)")
    sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break
    height = new_height

all_contents = driver.find_elements(By.TAG_NAME, "a")
for single_content in all_contents:
    print(single_content.text)

all_imgs = driver.find_elements(By.TAG_NAME, "img")
for single_img in all_imgs:
    print(single_img.get_attribute("src"))

driver.quit()