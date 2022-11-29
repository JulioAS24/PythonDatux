#8. Definir una función que imprima los argumentos ingresados desde linea de comandos
#Nota: Usar import sys.argv => *args



import sys
listaparametros=[]
def indeterminados_posicion(*args):
    args=sys.argv
    for arg in args:
        print("argumentos: ",args)
        print("cantidad de argumentos: ",len(args))
        listaparametros.append(arg)


indeterminados_posicion(sys.argv)
