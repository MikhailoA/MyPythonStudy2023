# convertation radians to degrees

pi = 3.14159265359
radian = float(input("Input radians: "))
degree = radian * (180 / pi)
print(round(degree, 5))

# convertation degrees to radians

degree = float(input("Input degree: "))
radian = degree * (pi / 180)
print(round(radian, 5))
