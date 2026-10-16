Что такое Page Object?

Это паттерн проектирования (шаблон), который помогает структурировать UI-тесты. Он отделяет описание страниц сайта от логики самих тестов.

Суть:
Представьте страницу вашего приложения как отдельный класс на Python. В этом классе вы описываете только то, что есть на странице:
кнопки, поля ввода, ссылки — их локаторы (как найти элемент) и методы работы с ними (нажать, ввести текст).

Зачем это нужно? (Преимущества)
Читаемость. Тест становится простым рассказом о действиях пользователя:
# Без page object:
driver.find_element(By.ID, "login").send_keys("user")

# С page object:
login_page = LoginPage(driver)      # Открываем страницу
login_page.enter_username("user")   # Читается как естественный язык!

Поддержка кода. Если разработчик поменял ID или CSS селектор элемента, вам нужно исправить его только в одном месте — внутри класса страницы. Все тесты сразу начнут работать правильно.
Повторное использование. Один и тот же класс LoginPage можно использовать во всех тестах, где нужен вход.

Как это работает на практике?
Шаг 1: Создаём файл с описанием страницы
# pages/login_page.py
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов (описание того, «где искать»)
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, ".password-input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Методы действий («что делать»)
    def enter_username(self, username):
        """Вводит имя пользователя"""
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def click_login_button(self):
        """Нажимает кнопку входа"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

⚠️ Важный момент: Внутри методов мы используем переменные‑локаторы (*self.USERNAME_FIELD), а не пишем пути напрямую. Это защищает нас от изменений верстки.

Шаг 2: Пишем сам тест
def test_successful_login(browser):  # Фикстура браузера из pytest-selenium
    # Подготовка: открываем страницу через её класс
    login_page = LoginPage(browser)
    browser.get("http://myapp.com/login")

    # Действия (читаются как сценарий пользователя)
    login_page.enter_username("admin")
    login_page.enter_password("secret")
    login_page.click_login_button()

    # Проверка результата
    dashboard_page = DashboardPage(browser)
    assert dashboard_page.is_user_logged_in(), "Пользователь не вошёл"


Типичные ошибки новичков:
Не создавать отдельные классы для каждой значимой страницы.
Писать слишком много логики проверки прямо внутрь классов страниц. Страница должна отвечать только за действия с элементами.
Забывать про наследование. Часто у разных страниц есть общие элементы (например, хедер с логотипом). Можно создать базовый класс BasePage.