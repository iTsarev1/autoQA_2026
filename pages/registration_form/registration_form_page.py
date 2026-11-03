from selene import have, command
from selene.support.shared import browser

from models import resource


class RegistrationForm:

    def __init__(self):
        self.uploadPicture = browser.element('#uploadPicture')

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=1).wait_until(have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_firstName(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def choose_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def choose_hobbies(self, value):
        browser.all('#hobbies-checkbox-2').element_by(have.value(value)).click()

    def choose_picture(self, value):
        self.uploadPicture.perform(command.js.scroll_into_view)
        browser.element('#uploadPicture').set_value(resource.path(value))

    def fill_current_address(self, value):
        browser.element('#currentAddress').perform(command.js.scroll_into_view)
        browser.element('#currentAddress').type(value)

    def choose_state_and_city(self, state, city):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()
        browser.element('#submit').perform(command.js.click)

    def should_registered_user_with(self, full_name, user_email, gender, user_number, birthday, subjects, hobbies, upload_picture,
                                    current_address, state_and_city):
        browser.element('Table').all('td').even.should(
            have.exact_texts(
                full_name, user_email, gender, user_number, birthday, subjects, hobbies, upload_picture, current_address, state_and_city
            )
        )