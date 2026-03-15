from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser, be, have

# Настройка профиля Chrome
options = Options()
options.add_argument(r'--user-data-dir=C:\Users\YourUser\AppData\Local\Google\Chrome\User Data\Profile Name')

browser.config.driver = webdriver.Chrome(options=options)