try:
    x = float(input("Введите любое число: "))
    if x > 0:
        print("Число положительное")
    elif x < 0:
        print("Число отрицательное")
    else:
        print("Число равно нулю")
except ValueError:
    print("Вы ввели не верное значение")

x = y = 1
while x < 10:
    while y < 10:
        print(f'{x} * {y} = {x * y}', end = ' | ')
        y += 1
    print()
    y = 1
    x += 1

print('-' * 100)

for x in range(1, 10):
    for y in range(1, 10):
        print(f'{x} * {y} = {x * y}', end = ' | ')
    print()