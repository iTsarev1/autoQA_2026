import pytest
import csv
from models.users import User


@pytest.fixture
def users() -> list[User]:
    with open("users.csv") as f:
        users = list(csv.DictReader(f))
    return [
        User(name=user["name"],
             age=int(user["age"]),
             status=user["status"],
             items=user["items"])
        for user in users
    ]


@pytest.fixture
def workers(users) -> list[User]:
    """
    Берем только работников из списка пользователей
    """
    workers = [user for user in users if user.status == "worker"]
    return workers


def users_are_adults(user: User):  # обозначаем, что функция на вход принимает класс User
    return user.age >= 18