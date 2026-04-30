for i in range(10):
    print(i)
print('-' * 100)


for i in range(1, 7):
    if i == 5:
        break
    print(i)
print('-' * 100)


for x in range(1,10):
    for y in range(1,10):
        print(f'{x} * {y} = {x * y}', end = ' | ')
    print()
print('-' * 100)


x = int(input("Введите любое целое число: "))
s = 0
while x > 0:
    s += x%10
    x = x//10
print("Сумма цифр введенного числа равна", s)
print('-' * 100)