import allure
from selene import browser

def test_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://https://github.com")
    with allure.step("Ищем репозиторий"):
        s(".header-search-input").click()
        s(".header-search -input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()