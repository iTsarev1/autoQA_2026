#Проверка, что selene и selenium импортированы в виртуальное окружение
try:
    import selene
    import selenium
    print("Selene и Selenium успешно импортированы!")
except ImportError as e:
    print(f"Произошла ошибка импорта: {e}")