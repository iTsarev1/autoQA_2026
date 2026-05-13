#homework all in

x = 1
y = "2"
print(x+int(y))

x = 33
number = x
number = 40
print(x, number)

# '''Выведи год рождения по возрасту'''
# x = input("Введите ваш возраст: ")
# print(2026 - int(x))

# '''Выведи какое число + - или =0'''
# try:
#     x = float(input("Введите любое число: "))
#     if x > 0:
#         print("Число положительное")
#     elif x < 0:
#         print("Число отрицательное")
#     else:
#         print("Число равно нулю")
# except ValueError:
#     print("Вы ввели брехню")


#Циклы

# '''Таблица умножения'''
# x = y = 1
# while x < 10:
#     while y < 10:
#         print(x, '*', y, '=', x * y, end=' | ')
#         y += 1
#     print()
#     y = 1
#     x +=1

# '''Посчитать сумму цифр введенного числа'''
# number = int(input("Введите целое число: "))
# s = 0
# while number > 0:
#     s += number % 10
#     number //=10
# print("Сумма цифр равна:", s)

'''FOR'''
for i in 1,2,"3три", "Четыре":
        print(i)
print('-' * 100)

s = "hello"
for i in s:
    print(i)
print('-' * 100)

for i in range(1, 10, 2):
    print(i)
print('-' * 100)

for i in range(10, 1, -1):
    print(i)
print('-' * 100)

'''Таблица умножения'''
for x in range(1, 10):
    for y in range(1, 10):
        print(f'{x} * {y} = {x * y}', end=' | ')
    print()
print('-' * 100)

'''Функция enumerate'''
s = 'hello'
for i in enumerate(s, 55):
    print(i)
print('-' * 100)

'''Функция break'''
s = 'hello'
for i in s:
    if i == 'l':
        break
    print(i)
print('-' * 100)

for i in range(20):
    if i == 11:
        break
    print(i)
print('-' * 100)

'''Функция continue'''
s = 'hello'
for i in s:
    if i == 'l':
        continue
    print(i)