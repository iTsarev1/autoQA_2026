from pages.registration_form.simple_user_registration_page import SimpleUserRegistrationPage

def test_registers_user():
    registration_page = SimpleUserRegistrationPage()

    registration_page.open()
