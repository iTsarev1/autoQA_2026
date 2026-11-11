from selene.support.shared import browser

class SimpleUserRegistrationPage:

    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('https://demoqa.com/text-box')

    def fill_full_name(self, value):
        self.full_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def fill_current_address(self, value):
        self.current_address.type(value)

    def fill_permanent_address(self, value):
        self.permanent_address.type(value)

    def submit(self):
        self.submit_button.click()