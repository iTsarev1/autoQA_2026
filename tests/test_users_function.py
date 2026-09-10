from fixtures.users_functions import *
import pytest
from allure import epic, feature, story, title, description, dynamic


@story("Функциональность работников")
@description("Тест проверяет, что работники совершеннолетние")
def test_users_are_adults_2(workers):
    for worker in workers:
        assert int(worker.age) >= 18