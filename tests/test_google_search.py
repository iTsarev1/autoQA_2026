from selene import browser, be, have
import time


def test_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qa guru').press_enter()