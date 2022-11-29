#3.Realizar un programa que dibuje un triángulo en consola
#  con * ,usando buclesn=int(input("Ingrese el número de renglones del triángulo: "))

n=int(input("Ingrese el número de filas del triángulo: "))

for i in range(n+1):
    espacios=n-i
    print(" "*espacios+"* "*i)

