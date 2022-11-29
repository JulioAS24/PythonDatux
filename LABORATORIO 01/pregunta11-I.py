#11.1  Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
#● Mostrar una suma de los dos números
#● Mostrar una resta de los dos números (el primero menos el segundo)
#● Mostrar una multiplicación de los dos números
#● En caso de introducir una opción inválida, el programa informará de que no es correcta.

num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
opcion=0

print("¿Qué operación requiere hacer? \n1) Sumar los 2 números \n2)Resta de los 2 números \n3) Multiplicación de ambos números")
opcion=int(input("Introduce el número de la opción: "))

if opcion==1:
    suma=num1 + num2
    print("La suma de ",num1,"+",num2,"es",suma)
elif opcion==2:
    resta=num1 - num2
    print("La resta de ",num1,"-",num2,"es",resta)
elif opcion==3:
    mul=num1 * num2
    print("El producto de ",num1,"*",num2,"es",mul)
else:
    print("La opción  es incorrecta")
    print("Escoger una de las tres opciones")

