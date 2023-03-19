#  Програма перевіряє чи існує трикутник по введеним сторонам та відображає його периметр та площу якщо він існує.

import math  # імпорт модулю math


def read_side():
    side = float(input("Введіть сторону трикутника: "))  # введення числа користувачем
    while side <= 0:  # перевірка, щоб число було додатне
        side = float(input("Спробуйте ще раз. Введіть додатнє число - сторону трикутника: "))
    return side


def is_triangle_exists(a, b, c):  # функція перевірки на існування трикутника
    if (a + b > c) and (b + c > a) and (a + c > b):
        return True
    else:
        return False


def calculate_perimeter(a, b, c):  # функція находження периметра
    return a + b + c


def calculate_area(a, b, c):  # функція находження площі
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


if __name__ == '__main__':
    a = read_side()  # сторона трикутника
    b = read_side()  # сторона трикутника
    c = read_side()  # сторона трикутника

    if is_triangle_exists(a, b, c):  # якщо трикутник існує - рахує периметр та площу і виводить на екран
        perimeter = calculate_perimeter(a, b, c)
        area = round(calculate_area(a, b, c), 3)
        print("Периметр трикутника: ", perimeter)
        print("Площа трикутника: ", area)
    else:  # якщо трикутник не існує
        print("Трикутник з такими сторонами не існує.")
