from fixtures.users_functions import *
import pytest

def test_users_are_adults_2(workers):
    """
    Тест проверяет, что работники совершеннолетние
    """
    for worker in workers:
        assert int(worker["age"]) >= 18