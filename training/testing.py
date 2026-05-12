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

'''Посчитать сумму цифр введенного числа'''
number = int(input("Введите целое число: "))
s = 0
while number > 0:
    s += number % 10
    number //=10
print("Сумма цифр равна:", s)