from selene import have, command
from selene.support.shared import browser


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
