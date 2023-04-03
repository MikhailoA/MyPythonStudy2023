# Функція перевірки на число
def get_number():
    while True:
        n = input('Скільки нотаток ви бажаєте побачити? ')
        if n.isdigit():
            return int(n)
        else:
            print('Введіть число!!!')


# Функція, що додає нотатки
def add_note():
    note = input('Введіть текст нотатки: ')
    notes.append(note)


# Функція, що виводить найраніші нотатки
def earliest_notes():
    n = get_number()
    for note in notes[:n]:
        print(note)


# Функція, що виводить найпізніші нотатки
def latest_notes():
    n = get_number()
    for note in notes[-n:]:
        print(note)


# Функція, що виводить нотатки за зменшенням довжини
def longest_notes():
    n = get_number()
    sorted_notes = sorted(notes, key=len, reverse=True)
    for note in sorted_notes[:n]:
        print(note)


# Функція, що виводить нотатки по зростанню довжини
def shortest_notes():
    n = get_number()
    sorted_notes = sorted(notes, key=len)
    for note in sorted_notes[:n]:
        print(note)


# Функція, яка зберігає нотатки у файл
def save_notes(filename):
    with open(filename, 'w', encoding='utf-8') as f:  # Відкриття файлу на запис
        for note in notes:
            f.write(note.strip() + '\n')


# Функція, що зчитує нотатки з файлу
def load_notes(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:  # Відкриття файлу на читання
            return f.readlines()
    except FileNotFoundError:
        print('Файл з нотатками не знайдено')
        return []


if __name__ == '__main__':
    save_file = input('Введіть назву файлу для зберігання нотаток: ')
    notes = load_notes(save_file)  # Завантаження нотаток з файлу
    while True:  # Діалог з користувачем
        command = input('Введіть команду (add, earliest, latest, longest, shortest, save & exit): ')
        if command == 'add':
            add_note()
        elif command == 'earliest':
            earliest_notes()
        elif command == 'latest':
            latest_notes()
        elif command == 'longest':
            longest_notes()
        elif command == 'shortest':
            shortest_notes()
        elif command == 'save & exit':
            save_notes(save_file)  # Збереження нотаток у файл
            print(f'Нотатки збережено у файлі {save_file} !')
            break
        else:
            print('Некоректна команда. Спробуй ще раз.')
