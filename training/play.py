# import random
#
# values = ["камень", "ножницы", "бумага"]
# player = input("Вы показали: ").lower() # добавил .lower(), чтобы можно было вводить любой литерал и код не падал
# if player not in values:
#     print(f'Значение {player} не корректно, допустимы: {values[0]}, {values[1]}, {values[2]}')
# else:
#     bot = random.choice(values)
#     print(f'Компьютер показал: {bot}')
#     wins = {
#         "камень": "ножницы",
#         "ножницы": "бумага",
#         "бумага": "камень"
#     }
#     if player == bot:
#         print("Ничья")
#     elif wins[player] == bot: # Допустим, игрок ввел player = "камень". Когда Python видит wins[player], он идет в словарь wins,
#                               # ищет ключ "камень" и достает связанное с ним значение. wins["камень"] вернет строку "ножницы"
#                               # "А не показал ли компьютер то, что бьется фигурой игрока?"
#         print("Ты победил")
#     else:
#         print("Компьютер победил")


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
































import random

values = ["камень", "ножницы", "бумага"]
player = input("Ваш ход: ").lower()
if player not in values:
    print(f'Значение {player} не корректное. Доступные значения: {values[0]}, {values[1]}, {values[2]}')
else:
    bot = random.choice(values)
    print(f'Компьютер показал: {bot}')
    wins = {
        "камень": "ножницы",
        "ножницы": "бумага",
        "бумага": "камень"
    }
    if player == wins:
        print("Ничья")
    elif wins[player] == bot:
        print("Ты выиграл")
    else:
        print("Ты проиграл")