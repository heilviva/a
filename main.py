import math

while True:
    print("Выберите операцию:")
    print("1. Сложить два числа")
    print("2. Вычесть одно число из другого")
    print("3. Умножить два числа")
    print("4. Разделить одно число на другое")
    print("5. Возвести число в степень N")
    print("6. Найти квадратный корень из числа")
    print("7. Найти синус числа")
    print("8. Найти косинус числа")
    print("9. Выйти из программы")

    choice = input("Ваш выбор: ")

    if choice == '9':
        break

    num1 = float(input("Введите первое число: "))
    if choice != '6' and choice != '7' and choice != '8':
        num2 = float(input("Введите второе число: "))

    if choice == '1':
        print( num1 + num2)

    elif choice == '2':
        print( num1 - num2)

    elif choice == '3':
        print(num1 * num2)

    elif choice == '4':
        if num2 == 0:
            print("Деление на ноль нельзя")
        else:
            print(num1 / num2)

    elif choice == '5':
        n = int(input("Введите степень: "))
        print(num1 ** n)

    elif choice == '6':
        if num1 < 0:
            print("Отрицательное число")
        else:
            print(math.sqrt(num1))

    elif choice == '7':
        print(math.sin(num1))

    elif choice == '8':
        print(math .cos(num1))

    elif choice == '9':
        break

    elif choice == '10':
        if num1 < 0:
            print("Отрицательное число")
        else:
            print(math.factorial(num1))
    else:
        print("Неверный выбор")
