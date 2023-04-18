from random import choices
from animals import Dog, Hen, Cow, Cat

if __name__ == '__main__':
    # Создание животных на ферме
    farm_animals = [
        Dog('Напас', {'мясо', 'сало', 'борщ'}, 14),
        Hen('Ряба', {"пшено", "крупа", "вода"}, 2),
        Cow('Бурёнка', {"трава", "сено"}, 5),
        Cat('Соня', {'сметана', 'хліб', 'молоко'}, 5)
    ]

    # пример полиморфизма - одинаковые названия функций, но разные классы и разная логика выполнения.
    food_to_offer = ['мясо', 'сало', 'борщ', 'пшено', 'крупа', 'вода', 'трава', 'сено', 'сметана', 'хліб', 'молоко']
    what_we_lost = list()  # Список, что мы теряем при кормлении животных
    what_we_get = list()  # Список, что мы получаем при уходе за животными
    for animal in farm_animals:
        print('\n', animal, type(animal))
        animal.say()
        for food in choices(food_to_offer, k=2):
            animal.eat(food)
            what_we_lost.append(food)
        what_we_get.append(animal.treat())
    print('-' * 60, f'\nСостояние животных :')

    for animal in farm_animals:  # Проверяем сыты ли животные
        if animal.hungry:
            print(f"На вашей ферме голодное животное! {animal}")
        else:
            print(f"{animal} сыта!")
    print('-' * 60, f'\nСостояние животных :')

    for animal in farm_animals:  # Проверяем настроение животных
        if not animal.good_mood:
            print(f"На вашей ферме грустное животное! {animal}")
        else:
            print(f"{animal} в отличном настроении!")

    print()
    print(f'Ухаживая за животными, мы потеряли: {what_we_lost}')
    print(f'Ухаживая за животными, мы получили: {what_we_get}')
