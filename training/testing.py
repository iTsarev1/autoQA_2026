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
print('-' * 100)


d = {
    "first": 1,
    "second": 2,
    "third": 3
}
for item in d:
    pprint(item)
print('-' * 100)

for item in d.keys():
    pprint(item)
print('-' * 100)

for item in d.values():
    pprint(item)
print('-' * 100)

for item in d.items():
    pprint(item)
print('-' * 100)

for (key, value) in d.items():
    pprint(f"Ключ: {key}, Значение: {value}")
print('-' * 100)


# RANGE

iteration_count = 10
for i in range(3, iteration_count, 2):
    print(f"Текущая итерация: {i}")
print('-' * 100)

iteration_count = 10
for i in range(iteration_count, 3, -1):
    print(f"Текущая итерация {i}")
print('-' * 100)


# CONTINUE
s = 10
for i in range(s):
    if i % 2 == 0:
        continue
    print(f"Точно НЕчетное число: {i}")
print('-' * 100)


# enumerate

cities = ["msk", "sar", "spb"]
i = 1
for city in cities:
    print(f"Город {city} на {i} месте по успешности")
    i += 1
print('-' * 100)

cities = ["msk", "sar", "spb"]
i = 1
for j, city in enumerate(cities, 1):
    print(f"Город {city} на {i} месте по успешности")
    i += 1