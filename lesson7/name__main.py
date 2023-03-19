# Програма повторює будь яку вашу вправу з HW 1. Вправи за типами даних int та float або HW 2.

def convert_radian_to_degree(radian):
    pi = 3.14159265359
    degree = radian * (180 / pi)
    return round(degree, 5)


if __name__ == '__main__':
    radian = float(input("Введіть радіани: "))
    degree = convert_radian_to_degree(radian)
    print(f'Градуси: {degree}')
