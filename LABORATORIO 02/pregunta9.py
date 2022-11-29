#9.Realizar una función que tenga por parámetro un lista de numeros y aumente cada elemento en +1

lista=[]
for valor in range(1,27):
    lista.append(valor)

def numerosAumen(lista):
    valor_incremental=1
    for numero in lista:
      PapaREDMAYNE=[numero+valor_incremental for numero in lista]
    return PapaREDMAYNE
    
grandeValera=numerosAumen(lista)



print(lista) # LISTA SIN MODIFICAR
print(grandeValera) 



