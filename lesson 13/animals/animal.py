from random import randint


class Animal:
    def __init__(self, name: str, preferred_food: set, age: int):
        """
        Конструктор класса Animal, который инициализирует атрибуты объекта
        :param name: имя животного
        :param preferred_food: перечень употребляемой еды
        :param age: возраст животного
        """
        self.name = name
        self.preferred_food = preferred_food
        self.age = age

        self.say_word = "???"
        self.animal_type = "Животное"
        self.__hungry = True  # изначально животное голодное
        self.good_mood = False  # изначально животное в плохом настроении

        # все поля класса должны задаваться в его конструкторе
        # представьте что какое-то свойство задаётся в одном методе, а используется в другом
        # где гарантии что методы будут вызваны в правильном порядке?
        # ведь если сначала прочитать еще несуществующее значение, будет ошибка
        # Чтобы её не было никогда, нужно объявлять атрибуты только в конструкторе класса
        # return self представьте что оно здесь так

    # getter - получатель, чтение свойства
    @property
    def hungry(self):
        return self.__hungry

    @hungry.setter
    def hungry(self, x):
        """
        Hungry может быть только булевым значением
        По логике работы программы можно только проголодаться
        Чтобы утолить голод, недостаточно присвоить False в hungry
        Нужно вызвать метод eat
        :param x:
        :return:
        """
        if isinstance(x, bool):
            if x:
                self.__hungry = True

    def good_mood(self, y):
        """
        Метод настроения животного
        меняеться на True, когда в методе treat мы заботимся о животном
        """
        if isinstance(y, bool):
            if y:
                self.good_mood = False

    def __str__(self):
        """
        return: возвращает строку с описанием животного.
        """
        return f"{self.animal_type} по имени {self.name}, {self.age} лет."

    def eat(self, food: str):
        """
        Метод проверяет голодное ли животное
        :param food: любимая еда животного
        """
        if food in self.preferred_food:
            print(f"{self.name} кушает {food}")
            self.__hungry = False
        else:
            print(f"{self.name} такое не ест: {food}")

    def say(self):
        """
        Метод "говорить", переопределяется наследниками
        """
        print(f"{self.name} говорит: {self.say_word}. Голод животного: {self.__hungry}")

    def treat(self, hours: int = randint(0, 3)):
        """
        Ухаживать за животным, переопределяется наследниками
        :param hours:
        :return:
        """
        print(f"Вы ухаживаете за {self.name} {hours} час(ов)")
        if self.__hungry:
            print(f"{self.name} голодное!")
