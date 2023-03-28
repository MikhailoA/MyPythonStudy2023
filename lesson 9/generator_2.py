def word_generator(s):
    # Розділяємо рядок на слова
    words = s.split()
    # Проходимося по кожному слову
    for word_gen in words:
        # Видаємо наступне слово
        yield word_gen


if __name__ == '__main__':
    s = input('Введіть строку!')
    generator = word_generator(s)

    for word in generator:
        print(word)
