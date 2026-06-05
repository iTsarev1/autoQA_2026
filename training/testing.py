x = 1
y = "2"
print(x+int(y))
print('-'*50)


# '''Выведи год рождения по возрасту'''
# x = input("Введите Ваш возраст: ")
# print("Ваш год рождения:", 2026-int(x))
# print('-'*50)


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
#     print("чупакабра")


x = y = 1
while x < 10:
    while y < 10:
        print(f'{x} x {y} = {x*y}', end=' | ')
        y +=1
    print()
    y =1
    x+=1
print('-'*50)


'''Посчитать сумму цифр введенного числа'''
number = int(input("Введите целое число: "))
s = 0
while number > 0:
    s += number %10
    number//=10
print(s)
print('-'*50)