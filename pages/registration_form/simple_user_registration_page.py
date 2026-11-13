from selene.support.shared import browser
from selene import have, command

class SimpleUserRegistrationPage:

    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('https://demoqa.com/text-box')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=1).wait_until(have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_full_name(self, value):
        self.full_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def fill_current_address(self, value):
        self.current_address.perform(command.js.scroll_into_view)
        self.current_address.type(value)

    def fill_permanent_address(self, value):
        self.permanent_address.type(value)

    def submit(self):
        self.submit_button.click()

    def should_have_submited(self, full_name, email, current_address, permanent_address):
        pass