import random

values = ["камень", "ножницы", "бумага"]
player = input("Вы показали: ")
bot = random.choice(values)
print(f'Компьютер показал: {bot}')
wins = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}
try:
    if player == bot:
        print("Ничья")
    elif wins[player] == bot:
        print("Ты победил")
    else:
        print("Компьютер победил")
except KeyError:
    print("Введенное значение не корректно. Разрешенные значения: камень, ножницы, бумага")