import  random

values = ["камень", "ножницы", "бумага"]

player = input("Твой ход: ")
bot = random.choice(values)
print("Компьютер:", bot)
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