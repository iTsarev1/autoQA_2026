# Объектно-ориентированная парадигма для построения модели для тестов

from pages.registration_form.registration_form_page import RegistrationForm


def test_student_registration_form():
    registration_form = RegistrationForm()
    # открыть форму регистрации
    registration_form.open()
    # вставить имя в строку
    registration_form.fill_firstName('Olga') # fill - вставляет всю строку целиком, type - посимвольно вводит текст, как живой человек
    # вставить фамилию в строку
    registration_form.fill_last_name('YA')
    # вставить email в строку
    registration_form.fill_email()
    # выбрать пол
    registration_form.choose_female()
    # вставить номер телефона в строку
    registration_form.fill_number()
    # выбрать дату рождения
    registration_form.fill_birthday('1999', 'May', '11')
    # вставить предметы в строку
    registration_form.fill_subjects()
    # вставить хобби в строку
    registration_form.choose_hobbies()
    # выбрать файл
    registration_form.choose_picture()
    # вставить адрес в строку
    registration_form.fill_current_address()
    # выбрать штат и город
    registration_form.choose_state_and_city()

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