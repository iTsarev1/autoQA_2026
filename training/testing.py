import random

required_number = 7
random_number = random.randint(1,10) # noqa

while required_number != random_number:
    random_number = random.randint(1,10)
    print(f"Пользователь ввел число: {random_number}")


iteration_count = 10
i = 1
while i < iteration_count:
    print(f"Текущая итерация: {i}")
    i +=1