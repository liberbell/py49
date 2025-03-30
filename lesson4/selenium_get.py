from selenium import webdriver


URL1= "https://www.google.com"
URL2 = "https://hosh-it.github.io/scraping-practice-selenium/"

options = get_default_chrome_options()
options.add_experimental_option("detach", True)
chrome = webdriver.Chrome()
chrome.get(URL2)


chrome.quit()