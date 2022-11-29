#15.iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad.
##Nota : cada elemento de la lista puede ser otra lista [[nombre,edad],....
listaInfo=[]
listaInfo=[['Oliver',15],['Benji',17],['Andy',22]]
for elemento in listaInfo:
    if elemento[1]>=18:
        print("La persona es mayor de edad",elemento[0])

        