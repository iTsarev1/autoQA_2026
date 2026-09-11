import pytest
import csv
from models.users import User, UserStatus


@pytest.fixture
def users() -> list[User]:
    with open("users.csv") as f:
        users = list(csv.DictReader(f))
    return [
        User(name=user["name"],
             age=int(user["age"]),
             status=UserStatus(user["status"]),
             items=user["items"])
        for user in users
    ]
# -> list[User] это аннотация типов. Он говорит: «Я сейчас скажу тебе тип того, что вернёт эта функция».
# Когда другой программист откроет твой файл, он сразу увидит: «Ага, эта штука мне отдаст именно список сотрудников!»,
# а не какие-нибудь числа или словарь

@pytest.fixture
def workers(users) -> list[User]:
    """
    Берем только работников из списка пользователей
    """
    workers = [user for user in users if user.status == UserStatus.worker]
    return workers


# def users_are_adults(user: User):  # обозначаем, что функция на вход принимает класс User
#     return user.age >= 18