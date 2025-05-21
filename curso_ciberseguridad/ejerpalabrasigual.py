p1 = input("Ingrese la primera palabra: ")
p2 = input("Ingrese la segunda palabra: ")

if p1.lower()==p2.lower():
    print("Ambas palabras son iguales")
else:
    print("Las palabras no son iguales")

if p1[0].lower()==p2[0].lower():
    print("Las dos palabras empiezan por la misma letra")
else:
    print("Las dos palabras empiezan por letras distintas")

if p1[-1].lower()==p2[-1].lower():
    print("Las dos palabras terminan \ncon la misma letra")
else:
    print("Las dos palabras terminan en letras distintas")