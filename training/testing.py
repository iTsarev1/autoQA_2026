def sum(a, b):
    return a + b

n = sum(1,2)
print(n)
print('-' * 100)


def return_tuple():
    return 1, 2, 3
n = return_tuple()
print(n)
print('-' * 100)


n1, n2, n3 = return_tuple()
print(n1, n2, n3)
print('-' * 100)


n1, *n2 = return_tuple()
print(n1, n2)
print('-' * 100)


#*args
def custom(*args):
    for arg in args:
        print(arg)

custom(1, 2, 3)
print('-' * 100)


def custom_2(*args):
    print(args)
    print(*args)

custom_2(1, 2, 3)
print('-' * 100)