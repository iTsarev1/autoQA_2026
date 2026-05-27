import pytest
from selene import browser
from config import config


@pytest.fixture
def login_page(browser):
    print("Логин пейдж!")


@pytest.fixture
def user():
    print("Юзер!")
    return "username", "password"


#берем фикстуру user и добавляем ее имя в аргументы нашего теста:
def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"


def test_logout(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"


@pytest.fixture(scope="function")  # scope="function" для каждого теста
def setup_browser():
    browser.config.base_url = config.BASE_URL
    browser.open(config.BASE_URL)  # Открываем браузер один раз для всех тестов
    yield
    # В конце теста очищаем состояние браузера
    # browser.element('[logout-button]').click()  # Пример выхода из аккаунта
    # Или очистка cookies
    browser.driver.delete_all_cookies()