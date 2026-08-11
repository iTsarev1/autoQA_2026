from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selene import query
import os
import requests

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "C:/Users/i.tsarev/PythonProjects/PythonProjectTsarev/tmp",
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver

browser.open("http://github.com/pytest-dev/pytest/blob/main/README.rst")
# browser.element("[data-testid='download-raw-button']").click()
download_url = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
print(download_url)
content = requests.get(url=download_url).content

with open("tmp/README.rst", "wb") as f:
    f.write(content)


with open("tmp/README.rst") as f:
    file_content_str = f.read()
    assert "test_answer" in file_content_str