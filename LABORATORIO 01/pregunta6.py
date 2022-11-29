
#6.Realice un programa que calcule la suma de los números hasta el valor ingresado.
#Ejemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5.

soma=0
valor=int(input("Ingrese valor: "))
for i in range(1,valor+1):
        soma+=i
print("La suma hasta el valor ingresado es : ",soma)
