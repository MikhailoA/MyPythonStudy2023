from random import randint, choices


class Cat:
    def __init__(
            self, name: str, gender: str, age: int,
            breed: str, play_hours: int, sleep_hours: int, preferred_food: set):
        """
        Конструктор класу Cat, який ініціалізує атрибути об'єкта.
        :param name: ім'я кота
        :param gender: стать
        :param age: вік
        :param breed: порода
        :param play_hours: часи гри
        :param sleep_hours: часи сну
        :param preferred_food: улюблена їжа
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed
        self.play_hours = play_hours
        self.sleep_hours = sleep_hours
        self.preferred_food = preferred_food
        self.hungry = False  # атрибут, що відслідковує, чи їла кішка
        self.played = False  # атрибут, що відслідковує, чи гуляла кішка

    def __str__(self) -> str:
        """
        :return: повертає рядок з описом кота
        """
        return f'{self.breed.title()}, {self.age} років, по імені {self.name}'

    def play(self):
        """
        Метод в якому описується поведінка кота коли гуляє/не гуляє
        """
        if self.play_hours == 0:  # Якщо години гри = 0, то кіт бажає гуляти.
            print(f'{self.name} хоче гуляти!!!')
            self.meow()
        else:
            print(f'{self.name} грає {self.play_hours} часів!')
            self.played = True  # позначаємо, що кішка гуляла
        self.hungry = True  # позначаємо, що кішка голодна

    def eat(self, some_food: str):
        """
        Метод, що призначений для годування кішки.
        :param some_food: улюблена їжа
        """
        if some_food in self.preferred_food:
            print(f'{self.name} їсть {some_food}. Киця вже не голодна!')
            self.hungry = False
        else:
            print(f'{self.name} дали їсти {some_food}, але вона це не їсть!')
            self.meow()

    def meow(self):
        """
        Метод що дозволяє мяукати
        """
        print(f'{self.name} мяукає!')

    def sleep(self):
        """
        Метод для сну кішки
        """
        if self.sleep_hours == 0:  # Якщо години сна = 0, то кіт бажає спати.
            print(f'{self.name} хоче спати!')
        else:
            print(f'{self.name} спить {self.sleep_hours} часів, відпочиває!!')


if __name__ == '__main__':
    # Створення об'єктів кішок з деякими випадковими параметрами.
    murka = Cat('Мурка', 'Ж', 8, 'Перська кішка', randint(0, 3), randint(0, 6), {'риба', 'мясо курки', 'молоко'})
    bysja = Cat('Буся', 'Ж', 5, 'Шотландська кішка', randint(0, 3), randint(0, 6), {'корм', 'мясо', 'кефір'})
    tom = Cat('Том', 'М', 6, 'Мейн-кун', randint(0, 3), randint(0, 6), {'риба', 'сухий корм', 'молоко'})
    barsik = Cat('Барсік', 'М', 9, 'Британський кіт', randint(0, 3), randint(0, 6), {'риба', 'борщ', 'молоко'})
    vaska = Cat('Васька', 'М', 7, 'Азійський кіт', randint(0, 3), randint(0, 6), {'риба', 'картопля', 'вода'})
    sonja = Cat('Соня', 'Ж', 5, 'Сіамська кішка', randint(0, 3), randint(0, 6), {'сметана', 'хліб', 'молоко'})

    # перелік їжі котів
    cats_food = ['рыба', 'мясо', 'мясо курки', 'молоко', 'корм', 'кефір',
                 'сухий корм', 'борщ', 'картопля', 'сметана', 'хліб', 'вода']

    hungry_cats = list()
    for cat in [murka, bysja, tom, barsik, vaska, sonja]:
        print('-' * 40, f'\nЗвичайний день {cat}:')
        cat.play()
        cat.sleep()
        for food in choices(cats_food, k=1):
            cat.eat(food)
        if cat.hungry:
            hungry_cats.append(cat)

    if hungry_cats:  # перевіряємо чи є голодні коти, якщо так, виводимо їхні імена.
        print('-' * 40, f'\nСтан тварин :')
        print(f'Сьогодні {len(hungry_cats)} голоді пухнастика, дайте їм поїсти!')
        print('Це:', ', '.join([cat.name for cat in hungry_cats]))

    played_cats = list()
    for cat in [murka, bysja, tom, barsik, vaska, sonja]:
        if cat.played:
            played_cats.append(cat)
    if played_cats:  # перевіряємо які коти гуляли, виводимо їхні імена
        print(f'Сьогодні {len(played_cats)} кицьок гуляли, вони добре провели час!')
        print('Це:', ', '.join([cat.name for cat in played_cats]))
    else:
        print('Сьогодні жодна кішка не гуляла :(')
