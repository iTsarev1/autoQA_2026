# Объектно-ориентированная парадигма для построения модели для тестов
from symtable import Class

from selene.support.shared import browser
from selene import have
from selene import command
from models import resource


class RegistrationForm:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=1).wait_until(have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_firstName(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def should_registered_user_with(self, full_name, user_email, gender, user_number, birthday, subjects, hobbies, upload_picture,
                                    current_address, state_and_city):
        browser.element('Table').all('td').even.should(
            have.exact_texts(
                full_name, user_email, gender, user_number, birthday, subjects, hobbies, upload_picture, current_address, state_and_city
            )
        )


def test_student_registration_form():
    registration_form = RegistrationForm()
    # открыть форму регистрации
    registration_form.open()

    registration_form.fill_firstName('Olga') # fill - вставляет всю строку целиком, type - посимвольно вводит текст, как живой человек
    registration_form.fill_last_name('YA')

    browser.element('#userEmail').type('name@example.com' )
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    browser.element('#userNumber').type('1234567891')
    registration_form.fill_birthday('1999', 'May', '11')

    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.all('#hobbies-checkbox-2').element_by(have.value('2')).click()
    browser.element('#uploadPicture').set_value(resource.path('foto.jpg'))
    browser.element('#currentAddress').type('Moscowskaya Street 18')
    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have. exact_text('Delhi')).click()
    browser.element('#submit').perform(command.js.click)

    # THEN
    # пользователь должен зарегистрироваться со следующими данными
    registration_form.should_registered_user_with(
        'Olga YA',
        'name@example.com',
        'Female',
        '1234567891',
        '11 May,1999',
        'Computer Science',
        'Reading',
        'foto.jpg',
        'Moscowskaya Street 18',
        'NCR Delhi'
    )