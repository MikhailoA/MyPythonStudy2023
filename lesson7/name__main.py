# Програма повторює будь яку вашу вправу з HW 1. Вправи за типами даних int та float або HW 2.
# конвертації радіан в градуси та градусів в радіани.

def convert_radians_to_degrees(radians):  # функція конвертації радіан в градуси.
    pi = 3.14159265359
    degrees = radians * (180 / pi)
    return round(degrees, 5)


def convert_degrees_to_radians(degrees):  # функція конвертації градусів в радіани.
    pi = 3.14159265359
    radians = degrees * (pi / 180)
    return round(radians, 5)


if __name__ == '__main__':
    print("Виберіть конвертацію:")  # діалог з користувачем.
    print("1. Радіани у градуси")
    print("2. Градуси у радіани")

    choice = int(input("Зробіть вибір (1 або 2): "))

    if choice == 1:
        radians = float(input("Введіть радіани: "))
        degrees = convert_radians_to_degrees(radians)
        print(f"{radians} радіан = {degrees} градусів")
    elif choice == 2:
        degrees = float(input("Введіть градуси: "))
        radians = convert_degrees_to_radians(degrees)
        print(f"{degrees} градусів = {radians} радіан")
    else:
        print("Не вірний вибір")
