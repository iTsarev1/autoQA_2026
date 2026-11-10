

class SimpleUserRegistrationPage:

    def __init__(self, browser):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.submit = browser.element('#submit')

    def fill_full_name(self, value):
        self.full_name.type(value)

    def fill_email(self, value):
        self.email.fill(value)

    def fill_current_address(self, value):
        self.current_address.fill(value)