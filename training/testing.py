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


# '''Посчитать сумму цифр введенного числа'''
# number = int(input("Введите целое число: "))
# s = 0
# while number > 0:
#     s += number %10
#     number//=10
# print(s)
# print('-'*50)


s = [1,2,3,4,5,6]
for i in s:
    print(i)
print('-'*50)

s = [1,2,3,4,5,6], 1, "hello"
for i in s:
        print(i)
print('-'*50)

for i in range(1, 5):
    print(i)
print('-'*50)

for i in range(5, 0, -1):
    print(i)
print('-'*50)


for x in range(1, 10):
    for y in range(1, 10):
       print(f'{x} * {y} = {x * y}', end=' | ')
    print()
print('-'*50)


'''enumerate'''
s = 'hello'
for i in enumerate(s, -1):
    print(i)
print('-' * 50)

'''break'''
s = 1, 2, 3, 4, 5, 6, 7
for i in s:
    if i == 5:
        break
    print(i)
print('-' * 50)

'''continue'''
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
print('-' * 50)

s = 'hello'
for i in s:
    if i == "l":
        continue
    print(i)

