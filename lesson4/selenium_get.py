from selenium import webdriver
from selenium.webdriver.common.by import By


URL1= "https://www.google.com"
URL2 = "https://hosh-it.github.io/scraping-practice-selenium/"

options = get_default_chrome_options()
options.add_experimental_option("detach", True)
chrome = webdriver.Chrome(options=options)

chrome.get(URL2)
chrome.quit()