numbers_sum = 0
while True:
    user_input = input("Введіть число або 'sum' для отримання суми: ")
    if user_input.lower() == "sum":  # якщо введено "sum", програма рахує суму та завершується
        print("Сума введених чисел:", numbers_sum)
        break
    elif user_input.replace('.', '').replace('-', '').isdigit():
        # Перевірка, чи є введене значення числом, включаючи від'ємні та дробові числа
        numbers_sum += float(user_input)  # додаємо введене число до змінної
    else:
        print("Помилка: введіть число або 'sum'.")  # Вивід помилки
