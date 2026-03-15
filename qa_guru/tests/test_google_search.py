from selene import (browser, be, have)
import time


def test_google_search():
    time.sleep(2)
    browser.open('https://google.com')
    time.sleep(2)
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    time.sleep(2)
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))