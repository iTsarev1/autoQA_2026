

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


print('-' * 100)


number = int(input('Введите любое целое число, а я выведу сумму цифр: '))
s = 0
while number > 0:
    s += number % 10
    number //= 10
print('Сумма равна:', s)


print('-' * 100)


s = 'hello'
for i in enumerate(s, 4):
    print(i)

print('-' * 100)


s = 'hello'
for i in s:
    if i == 'l':
        continue
    print(i)