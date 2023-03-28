def fibonacci_generator():  # Функцію-генератор послідовності чисел Фібоначчі.
    n = int(input("Введіть кінцевий індекс елементу послідовності Фібоначчі: "))
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    for number in fibonacci_generator():  # виклик функції
        print(number, end=' ')
