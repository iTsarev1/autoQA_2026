from data.users import User
from pages.registration_form.simple_user_registration_page import SimpleUserRegistrationPage

def test_registers_user():
    registration_page = SimpleUserRegistrationPage()
    ilya = User(full_name = 'Tsarev Ilya Vladimirovich', email = 'itsarev.111@gmail.com')

    registration_page.open()
    registration_page.fill_full_name(ilya.full_name)
    registration_page.fill_email(ilya.email)
    registration_page.fill_current_address('Saratov, Moscovskaya, 1/55, office 6')
    registration_page.fill_permanent_address('Saratov region')
    registration_page.submit()

    registration_page.should_have_submited('Tsarev Ilya Vladimirovich', 'itsarev.111@gmail.com')