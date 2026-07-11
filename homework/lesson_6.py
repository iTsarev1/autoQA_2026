from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # Логика: ночь считается с 22:00 до 06:00.
    if current_time >= time(22) or current_time <= time(6):
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # 1. Проверяем наличие выбора пользователя (приоритет №1)
    if dark_theme_enabled_by_user is not None:
        is_dark_theme = bool(dark_theme_enabled_by_user)
    else:
        # 2. Если выбора нет, применяем логику времени (ночь с 22 до 6)
        if current_time >= time(22) or current_time <= time(6):
            is_dark_theme = True
        else:
            is_dark_theme = False

    assert is_dark_theme is True
# Объяснение кода:
# 1. current_time = time(hour=16)
# Здесь мы создаем объект времени. Мы жестко задаем условие нашего теста: «Сейчас на часах 16:00». Минуты и секунды по умолчанию равны нулю.
# На данном этапе это просто данные-заглушка. В реальном UI-тесте вместо этой строки было бы обращение к системному времени компьютера (datetime.now().time()).

# 2. dark_theme_enabled_by_user = True
# Мы инициализируем переменную состояния настроек пользователя. Согласно описанию задания:
# True — пользователь сам зашел в настройки и принудительно включил темную тему.
# False — пользователь принудительно выключил её (хочет светлую даже ночью).
# None — пользователь ничего не трогал («Использовать системные настройки»).
# В нашем конкретном примере стоит True.

# 3. if dark_theme_enabled_by_user is not None:
# Это самая важная строчка, реализующая бизнес-правило приоритета. Оператор is not None проверяет, делал ли пользователь вообще какой-то осознанный выбор.
# Поскольку у нас значение равно True (а True определенно не является объектом None), условие срабатывает. Управление переходит внутрь блока if.

# 4. is_dark_theme = bool(dark_theme_enabled_by_user)
# Так как пользователь сделал выбор, система полностью игнорирует время суток. Она берет настройку пользователя и приводит её к строгому булевому типу (bool).
# Если там True, то is_dark_theme станет True.
# Если там False, то is_dark_theme станет False.
# Блок else (логика по времени) при этом полностью пропускается. Даже если сейчас глубокая ночь, но пользователь выбрал False, сайт останется светлым.

# 5. else: (внешний)
# Этот блок сработал бы только в одном случае: если бы переменная dark_theme_enabled_by_user была равна None. То есть человек отказался от ручного управления, отдав всё на откуп системе. Тогда программе пришлось бы смотреть на часы.

# 6. Внутренняя проверка времени: if current_time >= time(22) or current_time <= time(6):
# Эта логика работает только при отсутствии выбора пользователя. Здесь используется математическая особенность сравнения времени через оператор or:
# так как время не может быть одновременно "после 22" и "до 6", условие успешно ловит ночное окно, переходящее через полночь.
# >= time(22) — захватывает промежуток с 22:00 до 23:59.
# <= time(6) — захватывает промежуток с 00:00 до 06:00.
# Если оба условия ложны (сейчас день), выполняется ветка else ниже.

# 7. assert is_dark_theme is True
# Это финальная точка любого автотеста. Команда assert говорит интерпретатору: «Я утверждаю, что результат вычислений должен быть истиной.
# Если прямо сейчас переменная is_dark_theme содержит хоть что-то, кроме True (например, False или None), немедленно останови выполнение и пометь тест как проваленный».

# Почему наш конкретный пример проходит проверку
# Давайте проследим путь данных:
# Время установлено на 16:00 (день).
# Выбор пользователя установлен в True (он хочет темноту вручную).
# Код доходит до проверки if dark_theme_enabled_by_user is not None:. Результат — Да (это True).
# Выполняется присваивание: is_dark_theme = True.
# Код проскакивает всю логику про 22 часа и 6 утра, она ему неинтересна.
# Дохидт до assert is_dark_theme is True. Переменная действительно равна True.
# Тест завершается статусом PASSED (пройдено)


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = None
    for user in users:
        if user["name"] == "Olga":
            suitable_users = user

    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    # 1. Берем СТРОКУ с именем функции через .__name__ и сразу применяем к нему цепочку изменений
    actual_result = open_browser.__name__.replace("_", " ").title()
    # replace("_", " ") Меняет подчеркивание на пробел
    # title() делает большие первые буквы КАЖДОГО слова ("Open Browser"),а .capitalize() только самой первой буквы ("Open browser")

    actual_result = f"{actual_result} [{browser_name}]"
    print(actual_result)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = None
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = None
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"