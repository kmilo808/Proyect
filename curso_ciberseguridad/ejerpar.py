n1 = int(input("Inserte el primer numero: "))
n2 = int(input("Inserte el segundo numero: "))

p1 = n1%2
p2 = n2%2

if p1==0 and p2==0:
    print("Ambos numeros son pares")
elif p2==0:
    print("El segundo numero es par")
elif p1==0:
    print("El primer numero es par")
else:
    print("Ningun numero es par")  
