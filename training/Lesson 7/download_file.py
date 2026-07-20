from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_download():
    browser.open("http://github.com/pytest-dev/pytest/blob/main/README.rst")
    browser.element("[data-testid='download-raw-button']").click()