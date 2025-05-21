saldo=1000000

seleccion= int(input("Seleccione una opcion :\n1. Ingresar dinero\n2. Retirar dinero\n3. Mostrar saldo\n4. Salir\n- "))

if seleccion==1:
    ingreso=int(input("Cuanto dinero desea ingresar?: $"))
    confirmar=(input(f"Esta seguro de que ${ingreso} es la cantidad que desea ingresar? S/N :"))
    if confirmar.upper() =="S":
        saldo+=ingreso
        print("El dinero ha sido ingresado correctamente. Nuevo saldo : $",saldo)
    elif confirmar.upper() =="N":   
        print("No se realizo el ingreso. Su saldo es: $",saldo)
    else:
        print("Error: Por favor eliga una de las opciones que se esta solicitando")    

elif seleccion==2:
    retiro=int(input("Cuanto dinero desea retirar?: $"))         
    confirmar=(input(f"Esta seguro de que ${retiro} es la cantidad que desea retirar? S/N:"))
    if confirmar.upper() =="S":
            if retiro>saldo:
                print("El saldo en su cuenta es insuficiente. Su saldo es: $",saldo)
            else:
                saldo-=retiro
                print("El dinero se ha retirado correctamente. Nuevo saldo: $",saldo)
            
    elif confirmar.upper() =="N":   
            print("No se realizo el retiro. Su saldo es: $",saldo)
    else :
            print("Error: Por favor eliga una de las opciones que se esta solicitando")

elif seleccion==3:
    print("Su saldo es de: $",saldo)

elif seleccion==4:
    print("Proceso finalizado. Hasta la proxima")
else:
    print("Error: Por favor eliga una de las opciones que se esta solicitando")
