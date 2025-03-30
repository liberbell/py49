from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("webdriber/chromedriver")

webdriver.Chrome(service)