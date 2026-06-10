import random

# while - цикл с предусловием
# пример: пока пользователь не введет правильный номер, ...
# цикл while будет выполняться, пока выполняется какое-то условие


required_number = 7
user_number = random.randint(1,10)

while required_number != user_number:
    user_number = random.randint(1, 10)
    print(f"Пользователь ввел число: {user_number}")