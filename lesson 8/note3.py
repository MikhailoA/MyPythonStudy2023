'''def save_notes(notes):
    """Зберігає нотатки у файл"""

    filename = input("Введіть назву файлу для збереження нотаток: ")

    try:
        with open(filename, 'w') as file:
            for note in notes:
                file.write(note + '\n')
        print("Нотатки збережено у файлі", filename)
    except:
        print("Сталася помилка при збереженні нотаток у файлі", filename)

def load_notes():
    """Зчитує нотатки з файлу"""

    filename = input("Введіть назву файлу для завантаження нотаток: ")
    notes = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                notes.append(line.strip())
        print("Нотатки завантажено з файлу", filename)
    except:
        print("Сталася помилка при завантаженні нотаток з файлу", filename)

    return notes

def add_note():
    """Додає нову нотатку"""

    note = input("Введіть текст нотатки: ")
    return note

def display_notes(notes, sort_order, reverse_order, num_notes=None):
    """Виводить список нотаток у вказаному порядку"""

    if sort_order == 'earliest':
        notes = sorted(notes, reverse=reverse_order)
    elif sort_order == 'latest':
        notes = sorted(notes, reverse=not reverse_order)
    elif sort_order == 'longest':
        notes = sorted(notes, key=len, reverse=reverse_order)
    elif sort_order == 'shortest':
        notes = sorted(notes, key=len, reverse=not reverse_order)

    if num_notes:
        notes = notes[:num_notes]

    print("Список нотаток:")
    for note in notes:
        print(note)

def main():
    notes = load_notes()

    while True:
        command = input("Введіть команду (add, earliest, latest, longest, shortest, save & exit): ")

        if command == 'add':
            note = add_note()
            notes.append(note)
            print("Нотатка додана")

        elif command == 'earliest':
            num_notes = input("Введіть кількість нотаток, які бажаєте побачити: ")
            display_notes(notes, 'earliest', False, int(num_notes) if num_notes else None)

        elif command == 'latest':
            num_notes = input("Введіть кі'''




