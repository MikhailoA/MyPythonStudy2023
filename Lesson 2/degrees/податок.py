
a = float(input("Розмір надходження грн.: "))
b = 0.18  # есв 18%
c = 0.015  # війсковий збір 1.5%
налог = a * (b + c)
остаток = a - налог
print(round(налог, 2))
print(round(остаток, 2))
print(f'Налог:{налог} Остаток на счету:{остаток}')

# спросить за вывод со словами(....грн) и округлением до второго знака