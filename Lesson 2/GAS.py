# расчет потребления и цены газа

a = float(input("Показания текущие: "))
b = float(input("Показания прошлые: "))
с = 8.3 # тариф грн./м3
pay = (a - b)* с
print(f'Сума до сплати: {(round(pay, 2))} грн.')
