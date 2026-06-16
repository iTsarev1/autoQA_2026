import random


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
