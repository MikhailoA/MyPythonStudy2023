# Написати програму що рахує витрати на паливо.

a = float(input("Витрата палива авто: "))  # витрата палива на 100 км
b = float(input("Ціна палива: "))
e = float(input("Відстань км: "))
Витрата = ((a / 100) * b) * e
print(round(Витрата, 2))
print(f'Витрата коштів:{Витрата}')