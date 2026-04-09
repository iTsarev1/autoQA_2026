import pytest

@pytest.fixture
def browser():
    print("Браузер!")


@pytest.fixture
def login_page(browser):
    print("Логин пейдж!")


@pytest.fixture
def user():
    print("Юзер!")
    return "username", "password"


#берем фикстуру user и добавляем ее имя в аргументы нашего теста:
def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"