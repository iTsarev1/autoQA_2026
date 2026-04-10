import pytest


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


def test_logout(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"