from data import users
from pages.registration_form.simple_user_registration_page import SimpleUserRegistrationPage

def test_registers_user():
    registration_page = SimpleUserRegistrationPage()
    # ilya = User(full_name = 'Tsarev Ilya Vladimirovich', email = 'itsarev.111@gmail.com')
    admin = users.admin # чтобы было рядом, и было понятно, что откуда импортируется. чтобы не скролить вверх при длинном коде

    registration_page.open()
    registration_page.fill_full_name(admin.full_name)
    registration_page.fill_email(admin.email)
    registration_page.fill_current_address(admin.current_address)
    registration_page.fill_permanent_address(admin.permanent_address)
    registration_page.submit()

    registration_page.should_have_submited(admin.full_name, admin.email, admin.current_address, admin.permanent_address)