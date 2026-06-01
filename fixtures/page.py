from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser, be, have
import pytest
from config import config


# Настройка профиля Chrome --раньше использовались. взял из GPT
# options = Options()
# options.add_argument(r'--user-data-dir=C:\Users\YourUser\AppData\Local\Google\Chrome\User Data\Profile Name')
# browser.config.driver = webdriver.Chrome(options=options)


@pytest.fixture(scope="function")  # scope="function" для каждого теста
                                   # autouse = True - можно прописать, и тогда не надо будет в каждом тесте в аргументе указывать
def setup_browser():
    options = webdriver.ChromeOptions() #Создаём объект ChromeOptions, который позволяет настраивать параметры Chrome
    options.headless = True # Поменяй на False, чтобы открыть браузер

    browser.config.driver = webdriver.Chrome(options=options)
    browser.config.base_url = config.BASE_URL
    # browser.config.driver_options = webdriver.FirefoxOptions() # Чтобы принудительно открыть в Firefox, а не Chrome
    browser.open(config.BASE_URL)  # Открываем браузер один раз для всех тестов

    yield
    # В конце теста очищаем состояние браузера. очистка cookies browser.driver.delete_all_cookies()
    browser.quit() # закрывает браузер в конце каждого теста, чтобы тесты были независимы друг от друга