# програма що рахує податок від надхождення на рахунок підприємця.

a = float(input("Розмір надходження грн.: "))
b = 0.18  # єсв 18%
c = 0.015  # війсковий збір 1.5%
Податок = a * (b + c)
Залишок = a - Податок
print(f'Податок: {(round(Податок, 2))} грн. \nЗалишок на рахунку: {(round(Залишок, 2))} грн.')
