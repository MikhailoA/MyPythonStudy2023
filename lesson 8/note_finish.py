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


# Функція, яка пропонує користувачу вводити команди та опрацьовує їх
if __name__ == '__main__':
    notes = []  # Список для зберігання нотаток
    while True:  # Діалог з користувачем
        command = input('Введіть команду (add, earliest, latest, longest, shortest, exit): ')
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
        elif command == 'exit':
            print('До зустрічі!!!')
            break
        else:
            print('Некоректна команда. Спробуй ще раз.')
