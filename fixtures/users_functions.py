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


# def test_users_are_adults_2(workers):
#     """
#     Тест проверяет, что работники совершеннолетние
#     """
#     for worker in workers:
#         assert int(worker["age"]) >= 18