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


def get_user(user):
    return user["name"]

get_user({"name": "Olga", "age": 45})


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
            print(user)

    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = None
    for user in users:
        if user["age"] < 20:
            print(user)

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