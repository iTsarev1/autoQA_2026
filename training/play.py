import random

values = ["камень", "ножницы", "бумага"]
player = input("Вы показали: ").lower() # добавил .lower(), чтобы можно было вводить любой литерал и код не падал
if player not in values:
    print(f'Значение {player} не корректно, допустимы: {values[0]}, {values[1]}, {values[2]}')
else:
    bot = random.choice(values)
    print(f'Компьютер показал: {bot}')
    wins = {
        "камень": "ножницы",
        "ножницы": "бумага",
        "бумага": "камень"
    }
    if player == bot:
        print("Ничья")
    elif wins[player] == bot:
        print("Ты победил")
    else:
        print("Компьютер победил")


# упрощенная версия, не предусматривающая ввод не корректного значения и литерала:

# values = ["камень", "ножницы", "бумага"]
# player = input("Вы показали: ")
# bot = random.choice(values)
# print(f'Компьютер показал: {bot}')
# wins = {
#     "камень": "ножницы",
#     "ножницы": "бумага",
#     "бумага": "камень"
# }
# if player == bot:
#     print("Ничья")
# elif wins[player] == bot:
#     print("Ты победил")
# else:
#     print("Компьютер победил")