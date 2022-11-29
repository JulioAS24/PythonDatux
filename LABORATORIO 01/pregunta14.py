#14.Realice un Menú interactivo que tenga las opciones de saludar ,una operación matemática y salir.

n1=float(input("Ingrese un numero n1: "))
n2=float(input("Ingrese un numero n2: "))
n3=float(input("Ingrese un numero n3: "))
opcion=0
print("BIENVENIDOS AL MENU INICIO \n1)Saludar \n2)Sumar \n3)Salir ")
opcion=int(input("introduce el número de la opción: "))

if opcion==1:
    print("Bienvenido, Saludos Cordialmente")
    
elif opcion==2:
        suma=n1 + n2 +n3
        print("La suma de los numeros es: ",suma)
elif opcion==3:
        print("Salir")

        