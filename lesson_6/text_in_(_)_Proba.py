text = input("Введите текст: ")
output = ""

while '(' in text and ')' in text:
    start_index = text.index('(')
    end_index = text.index(')')
    output += text[:start_index - 1]
    text = text[end_index + 1:]

output += text

print(output)

#  Написати програму що видаляє те що написано в дужках (), залишивши весь інший текст.
#  Наприклад з "Я не знав куди йти (втім не дивно), тому пішов..." вийде "Я не знав куди йти, тому пішов..."

text = input("Введіть текст: ")  # введення тексту користувачем
while "(" in text and ")" in text:  # початок циклу
    start = text.find('(')  # пошук "("
    end = text.find(')', start)  # пошук ")"
    text1 = text[:start - 1] + text[end + 1:]  # зьєднування строк
    print(text1)  # вивод на екран редагованної строки
    break
else:
    print(text)