from .animal import Animal
from random import randint


class Cat(Animal):
    """
    класс Cat наследник класса Animal
    изменяет аргументы "say_word" и "animal_type" на своё
    """
    def __init__(self, name: str, preferred_food: set, age: int):
        super().__init__(name, preferred_food, age)
        self.say_word = "Мяу-Мяу!"  # что произносит животное
        self.animal_type = "Кіт"  # инициализирует животное

    def treat(self, hours: int = randint(0, 3)) -> str:
        """
        Метод, который показывает достаточно ли ухаживали за животным
        если достаточно, то атрибут "good_mood = True"
        :param hours: количество часов ухаживания за животным
        :return: возвращает продукт/настроение в зависимости от часов ухода за животным
        """
        if hours <= 1:
            print(f"Вам нужно больше ухаживать за {self.name}! Вы ухаживаете всего {hours} часов.")
            return "нема гарного настрою"
        else:
            print(f"Вы ухаживаете за {self.name} {hours} часов и у нас поднимается настроение.")
            self.good_mood = True
            return "Гарний настрій"
