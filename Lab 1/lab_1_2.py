print("Программа 'Общество в начале XXI века'")

while True:
    
    age_str = input("Введите ваш возраст (или 'выход' для завершения программы): ")

    if age_str.lower() == 'выход':
        break

    try:
        age = int(age_str)
    except ValueError:
        print("Ошибка! Введите корректное число или 'выход' для завершения программы.")
        continue

    if age >= 0 and age <= 7:
        print("Вам в детский сад")
    elif age > 7 and age <= 18:
        print("Вам в школу")
    elif age > 18 and age <= 25:
        print("Вам в профессиональное учебное заведение")
    elif age > 25 and age <= 60:
        print("Вам на работу")
    elif age > 60 and age <= 120:
        print("Вам предоставляется выбор")
    else:
        print("Ошибка! Это программа для людей!")
