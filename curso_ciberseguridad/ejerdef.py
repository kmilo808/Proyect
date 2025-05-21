def op(n1, n2):
    suma = n1 + n2
    resta = n1 - n2
    multiplicacion = n1 * n2
    division = n1 / n2 if n2 != 0 else "Indefinido"
    return suma, resta, multiplicacion, division

numeros = op(8, 2) 

print(f"Suma: {numeros[0]}")
print(f"Resta: {numeros[1]}")
print(f"Multiplicación: {numeros[2]}")
print(f"División: {numeros[3]}")
