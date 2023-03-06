print("Доброго вечора, я бот з України!")

while True:
    user_input = input("Користувач: ")
    if "привіт" in user_input.lower() or "хай" in user_input.lower() or "доброго дня" in user_input.lower():
        print("Бот: Доброго вечора, я бот з України!")
    elif "як справи" in user_input.lower() or "що робиш" in user_input.lower() or "чим займаєшся" in user_input.lower():
        print("Бот: Вчусь програмувати на Python!")
    elif "фільм" in user_input.lower() or "кінотеатр" in user_input.lower() or "серіал" in user_input.lower():
        print("Бот: Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал/фільм ваша відповідь, він просто бомба!")
    elif "бувай" in user_input.lower() or "надобраніч" in user_input.lower() or "гудбай" in user_input.lower() or "до зустрічі" in user_input.lower():
        print("Бот: Побачимось у мережі, I'll be back.")
        break
    else:
        print("Бот: Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
