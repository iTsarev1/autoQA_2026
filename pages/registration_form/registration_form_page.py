from selene import have, command
from selene.support.shared import browser

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

    def fill_email(self):
        browser.element('#userEmail').type('name@example.com')

    def choose_female(self):
        browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()

    def fill_number(self):
        browser.element('#userNumber').type('1234567891')

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def fill_subjects(self):
        browser.element('#subjectsInput').type('Computer Science').press_enter()

    def choose_hobbies(self):
        browser.all('#hobbies-checkbox-2').element_by(have.value('2')).click()

    def choose_picture(self):
        browser.element('#uploadPicture').set_value(resource.path('foto.jpg'))

    def fill_current_address(self):
        browser.element('#currentAddress').perform(command.js.scroll_into_view)
        browser.element('#currentAddress').type('Moscowskaya Street 18')

    def choose_state_and_city(self):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Delhi')).click()
        browser.element('#submit').perform(command.js.click)

    def should_registered_user_with(self, full_name, user_email, gender, user_number, birthday, subjects, hobbies, upload_picture,
                                    current_address, state_and_city):
        browser.element('Table').all('td').even.should(
            have.exact_texts(
                full_name, user_email, gender, user_number, birthday, subjects, hobbies, upload_picture, current_address, state_and_city
            )
        )