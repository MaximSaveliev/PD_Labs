x = int(input("Введите число от 1 до 9: "))


if 1 <= x <= 3:
    s = input("Введите строку: ")
    n = int(input("Введите количество повторов строки: "))
    result = s * n
    print("Результат работы цикла:")
    print(result)

elif 4 <= x <= 6:
    m = int(input("Введите степень для возведения числа: "))
    result = x ** m
    print("Результат возведения числа в степень:")
    print(result)


elif 7 <= x <= 9:
    for i in range(1, 11):
        x += 1
        print(x)

else:
    print("Ошибка ввода")
