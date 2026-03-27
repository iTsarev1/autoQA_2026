from selene import (browser, be, have)
import time
from allure import epic, feature, story, title, description, dynamic
from pytest import mark



class TestLogin:
    @story("Авторизация на QA Guru")
    @description("Тест проверяет успешную авторизацию")
    def test_login_qa_guru(self):
        time.sleep(1)
        browser.open('config.BASE_URL')
        time.sleep(1)
        browser.element('[name="email"]').should(be.blank).type("USER_LOGIN")
        time.sleep(1)
        browser.element('[name="password"]').should(be.blank).type('USER_PASSWORD').press_enter()
        time.sleep(1)
        browser.element('[class="stream-title"]').should(have.text('QA.GURU | Курс-интенсив: ChatGPT для тестировщиков'))
        #('[class="stream-title"]') можем записать проще: ('.stream-title')
        time.sleep(3)
        browser.close()

    @story("Авторизация на QA Guru")
    @description("Тест проверяет вывод Неверный пароль при неверных логопасах")
    def test_invalid_password(self):
        browser.open('https://school.qa.guru/')
        time.sleep(1)
        browser.element('[name="email"]').should(be.blank).type("yurapwnz1992@yandex.ru")
        time.sleep(1)
        browser.element('[name="password"]').should(be.blank).type('23fff34f').press_enter()
        browser.element('.btn-error').should(have.text('Неверный пароль'))
        browser.close()

    @story("Авторизация на QA Guru")
    @description("Тест проверяет вывод Не заполнено поле Пароль при не заполненном пароле")
    def test_empty_password(self):
        browser.open('https://school.qa.guru/')
        time.sleep(1)
        browser.element('[name="email"]').should(be.blank).type("yurapwnz1992@yandex.ru")
        time.sleep(1)
        browser.element('[name="password"]').press_enter()
        browser.element('.btn-error').should(have.text('Не заполнено поле Пароль'))





