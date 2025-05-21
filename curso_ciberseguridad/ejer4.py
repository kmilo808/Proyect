a = int(input("a: "))
b = int(input("b: "))


print(f"Valor original de a = {a}")
print(f"valor original de b = {b}")

c = a
a = (a+b)-a
b = c

print(f"Valor intercambiado de a = {a}")
print(f"valor intercambiado de b = {b}")
