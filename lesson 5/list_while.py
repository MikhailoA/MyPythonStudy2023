numbers = []  # список для зберігання введених чисел
while True:
    user_input = input("Введіть число або 'sum' для отримання суми: ")  # Користувач вводить числа
    if user_input.lower() == 'sum':  # умова циклу
        total = 0  # змінна для зберігання суми
        for j in numbers:
            total += j  # в змінну total додається змінна j
        print('Сума введених чисел: ', total)  #
        break  #
    elif user_input.replace('-', '').replace('.', '').isdigit():  #
        j = float(user_input)  #
        numbers.append(j)  #
    else:
        print("Будь ласка, введіть число або 'sum' для отримання суми.")  #
