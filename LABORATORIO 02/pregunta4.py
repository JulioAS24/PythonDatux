#4. Realizar un programa que inserte valores en una lista desde el 1 hasta el 100 saltando en
#2 en 2 . Ejemplo : [ 1,3 ,5 ,...]

lista=[]
for valor in range(1,101):
    lista.append(valor)

def extraer_impares(lista):
    impares=[]
    for n in lista:
        if n%2 !=0:
            impares.append(n)
    return impares

resultado=extraer_impares(lista)
print(resultado)

