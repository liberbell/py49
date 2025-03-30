from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("webdriber/chromedriver")

chrome = webdriver.Chrome()