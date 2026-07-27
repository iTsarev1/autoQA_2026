import random
from pprint import pprint

required_number = 7
random_number = random.randint(1,10) # noqa

while required_number != random_number:
    random_number = random.randint(1,10)
    print(f"Пользователь ввел число: {random_number}")
print('-' * 100)


iteration_count = 10
i = 1
while i < iteration_count:
    print(f"Текущая итерация: {i}")
    i +=1
print('-' * 100)


users = [
    {"name": "Ilya", "age": 32},
    {"name": "Elena", "age": 22},
    {"name": "Vasya", "age": 5},
    {"name": "Petya", "age": 3},
    {"name": "Klava", "age": 24}
]

for user in users:
    pprint(f"Пользователю {user['name']} {user['age']} лет")

