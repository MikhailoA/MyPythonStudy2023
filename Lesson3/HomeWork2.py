# Написати програму, що проводить невеличкий діалог з користувачем:

a = input('Please, input your string:')  # Ввод строки
b = input('What do you want to replace?')  # Ввод слова которое хотим заменить
print(b)
a.find(b)  # Поиск слова которое хотим заменить
print(f'{b} was found at position {a.find(b)}!')
c = input('With what do you want to replace?')  # Ввод слова на которое хотим заменить
print(c)
a = a.replace(b, c)  # Замена слова
a = a.lower()  # Перевод в нижний регистр
a = a.replace('.', '').replace(',', '').replace(':', '').replace('-', '') \
    .replace(';', '').replace('!', '').replace('?', '').replace(')', '')  # круглой скобки в примере нет)
a = a.rstrip()  # Убираем пробел справа
print(f'Here is your result: \n{a}')  # Вывод отформатированной строки
