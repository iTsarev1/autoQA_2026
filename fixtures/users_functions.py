import pytest
import csv


@pytest.fixture
def users():
    with open("users.csv") as f:
        users = list(csv.DictReader(f))
    return users


@pytest.fixture
def workers(users):
    """
    Берем только работников из списка пользователей
    """
    workers = [user for user in users if user["status"] == "worker"]
    return workers


def test_users_are_adults_2(workers):
    """
    Тест проверяет, что работники совершеннолетние
    """
    for worker in workers:
        assert int(worker["age"]) >= 18