a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
resultado = ((c+5)*(b**2-3*a*c)*a**2)/4*a
#print(resultado)
suma = c+5
potencia = b**2
resta = potencia-3*a*c
potencia2 = a**2
r = suma*resta*potencia2
div = r/4*a
print(f"({c}+5)({b}**2-3*{a}*{c}){a}**2/{a}**2")
print(f"    {suma}*{resta}*{potencia2}/4*{a}")
print(f"      {r}/{4*a}")
print(f"       {resultado}")