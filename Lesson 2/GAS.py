# расчет потребления и цены газа

a = float(input("Показания текущие: "))
b = float(input("Показания прошлые: "))
с = 8.3 # грн
pay = (a - b)* с
print(round(pay, 2))
