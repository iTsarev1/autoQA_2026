x = 1
y = 2
print(x+y)

x = 1
y = "2"
print(x + int(y))


x = r = 1
while x < 10:
    while r < 10:
        print(x, "*", r, "=", x * r, end = " | ")
        r +=1
    print()
    r = 1
    x += 1


s = "hello"
for i in s:
    print(i)
print("-"*30)

for i in range(2, 10, 2):
    print(i)
print("-"*30)

for i in range(10, 0, -1):
    print(i)
print("-"*30)

for x in range(1, 10):
    for y in range(1, 10):
        print(f'{x} * {y} = {x * y}', end = " | ")
    print()

s = "hello"
for i in enumerate(s, 1):
    print(i)

s = "hello"
for i in range(10):
    if i == 7:
        break
    print(i)