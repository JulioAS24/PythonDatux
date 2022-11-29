#1.Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el número.

lista=[]
for valor in range(1,101):
    lista.append(valor)

for elemento in lista:
    if elemento%2==0:
        print("Es múltiplo de 2:  ",elemento)
