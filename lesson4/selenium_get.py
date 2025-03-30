from selenium import webdriver
from selenium.webdriver.common.by import By

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
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")