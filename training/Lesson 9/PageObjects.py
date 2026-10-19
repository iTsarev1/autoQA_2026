# Объектно-ориентированная парадигма для построения модели для тестов

from selene.support.shared import browser
from selene import have
from selene import command
from models import resources


def test_student_registration_form():
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(have.size_greater_than_or_equal(3))
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

# WHEN
browser.element('#firstName').type('Olga')
browser.element('#lastName').type('YA')
browser.element('#userEmail').type('name@example.com' )
browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
browser.element('#userNumber').type('1234567891')
browser.element('#subjectsInput').type('Computer Science').press_enter()
browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
browser.element('#uploadPicture').set_value(resources.resource_path('foto.jpg'))
browser.element('#currentAddress').type('Moscowskaya Street 18')
browser.element('#state').perform(command.js.scroll_into_view)
browser.element('#state').click()
browser.all('[id^=react-select][id*=option]').element_by(have.exact_text( 'NCR')).click()
browser.element('#city').click()
browser.all('[id^=react-select][id*=option]').element_by(have. exact_text('Delhi')).click()
browser.element('#submit').perform(command.js.click)