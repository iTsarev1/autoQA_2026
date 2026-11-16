import random

values = ["камень", "ножницы", "бумага"]
player = input("Вы показали: ").lower() # добавил .lower(), чтобы можно было вводить любой литерал и код не падал
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
    print(f'Введенное Вами значение {player} не корректно. Разрешенные значения: камень, ножницы, бумага')