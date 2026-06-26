import random
from os import name

# while - цикл с предусловием
# пример: пока пользователь не введет правильный номер, ...
# цикл while будет выполняться, пока выполняется какое-то условие

required_number = 7
user_number = random.randint(1,10)

while required_number != user_number:
    user_number = random.randint(1, 10)
    print(f"Пользователь ввел число: {user_number}")
print('-' * 100)


# Пример ситуации, когда операция должна быть выполнена лимитированное кол-во раз:
iteration_count = 10
i = 0
while i < iteration_count:
    print(f"Текущая итерация: {i}")
    i += 1
print('-' * 100)


# Цикл for - используется для того, чтобы итерироваться по каким-либо коллекциям, спискам, словарям, строкам


# Итерируем списки
users = [
    {"name": "Ilya", "age": 32},
    {"name": "Elena", "age": 22},
    {"name": "Vasya", "age": 5},
    {"name": "Petya", "age": 3},
    {"name": "Klava", "age": 24}
]


from pprint import pprint

for user in users:
    pprint(f"Пользователю {user['name']} {user['age']} лет")
print('-' * 100)


# Итерируем словари

d = {
    "first": 1,
    "second": 2,
    "third": 3
}
for item in d:
    pprint(item)
print('-' * 100)
# эта строка идентична строке ниже:
for item in d.keys(): # Возвращает ключи
    pprint(item)
print('-' * 100)


for item in d.values(): # Возвращает значение
    pprint(item)
print('-' * 100)

for item in d.items(): # Возвращает пары в виде кортежей
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
    print(f"Текущая итерация: {i}")
print('-' * 100)


# break, continue, else - прерывание цикла

s = 10
for i in range(s):
    if i % 2 == 0:
        continue
    print(f"Точно четное число: {i}")
print('-' * 100)


# enumerate

cities = ["ЕКТБ", "Москва", "Челябинск"]
i = 1
for city in cities:
    print(f"{city} на {i} месте по загрязнению воздуха")
    i += 1
print('-' * 100)


cities = ["ЕКТБ", "Москва", "Челябинск"]
for j, city in enumerate(cities, 1):
    print(f"{city} на {j} месте по загрязнению воздуха")


cities = ["ЕКТБ", "Москва", "Челябинск"]
for city, j in enumerate(cities, 1):
    print(f"{city} на {j} месте")
# получиться чушь