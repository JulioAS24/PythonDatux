
#2. Realizar un programa que dibuje un cuadrado en consola con * ,usando bucles 
m=int(input("Ingrese el número de filas: "))
n=int(input("Ingrese el número de columnas: "))
for i in range (1,m+1):
    for j in range(1,n+1):
        print("*",end="  ")
    print(" ")


