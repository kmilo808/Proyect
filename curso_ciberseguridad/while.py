"""i = 1
nombre = "camilo ayala"
while i<=20:
   print("Numero: ", i,"Nombre: ",nombre)
   i+=1
"""
import math
n = int(input("ingrese un numero para sacar su raiz cuadrada: "))
while n<0:
    print("El numero tiene que ser positivo")
    n = int(input("vuelve a ingresar un numero: "))
print(f"la raiz cuadrada es: {math.sqrt(n)}")