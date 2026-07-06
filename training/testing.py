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