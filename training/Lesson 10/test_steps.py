import allure
from selene import browser
from selene.support.shared.jquery_style import s
from selene import by

def test_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")
    with allure.step("Ищем репозиторий"):
        browser.element("button[type='button'][aria-label='Search or jump to, type / to search']").click()
        browser.element("input[type='text'][aria-label='Search or jump to']").type("eroshenkoam/allure-example").press_enter()
    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Нажимаем на таб Issues"):
        browser.element("#.issues-tab").click()