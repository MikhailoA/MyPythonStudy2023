#  Програмa що читає текстовий файл та, використовуючи тільки list comprehension

with open("input.txt", "r") as file:  # Відкриваємо файл на читання
    lines = [line[line.find('a'):]  # Знаходимо "а", обрізаємо букви до неї.
             .strip().capitalize()  # Видаляємо \n. Робимо заглавну букву
             for line in file.readlines()  # Построчно зчитуємо файл
             if 'a' in line.lower()]  # Переводимо у нижній регістр
print(lines)
