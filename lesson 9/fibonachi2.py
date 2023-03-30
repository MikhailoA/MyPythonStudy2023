def fibonacci_generator():  # Функцію-генератор послідовності чисел Фібоначчі.
    while True:
        try:
            n = int(input("Введіть кінцевий індекс елементу послідовності Фібоначчі: "))
            a = 0
            b = 1
            for i in range(n):
                yield a
                a, b = b, a + b
            return a, b
        except Exception:
            print('Введіть ціле число!!!')


if __name__ == '__main__':
    for number in fibonacci_generator():  # виклик функції
        print(number, end=' ')
