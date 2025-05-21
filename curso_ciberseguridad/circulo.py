import math

r = float(input("Ingrese el valor del radio: "))

if r > 0:
    area = math.pi * r**2
    longitud = 2 * math.pi * r
    print("El valor del área es:", round(area, 2))
    print("El valor de la longitud es:", round(longitud, 2))
else:
    print("El radio debe ser positivo")

