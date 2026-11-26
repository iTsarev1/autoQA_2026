import allure

def test_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://https://github.com")
