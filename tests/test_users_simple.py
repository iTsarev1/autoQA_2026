import csv


# Тест проверяет, что все работники совершеннолетние
def test_users_are_adults():
    with open("users.csv") as f:
        users = csv.DictReader(f)
        # для каждого юзера из списка юзеров, если статус этого юзера = 'worker', возьми его и положи в результирующий список
        workers = [user for user in users if user["status"] == "worker"]
    for worker in workers:
        assert int(worker["age"]) >= 18
