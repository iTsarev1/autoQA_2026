try:
    x = float(input("Введите любое число: "))
    if x > 0:
        print("Число положительоне")
    elif x < 0:
        print("Число отрицательоне")
    else:
        print("Число равно нуля")
except ValueError:
    print("Вы ввели чехарду")