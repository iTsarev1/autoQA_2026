for x in range(1,10):
    for y in range(1,10):
        print(f'{x} * {y} = {x * y}', end = ' | ')
    print()



x = int(input("Введите любое целое число: "))
s = 0
while x > 0:
    s += x%10
    x = x//10
print("Сумма цифр введенного числа равна", s)