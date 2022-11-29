#11.2 Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.
letra=input("Ingrese una letra: ")
if len(letra)<2:
    if letra=="a":
        print("la letra ",letra,"Es vocal")
    elif letra=="e":
        print("la letra ",letra,"Es vocal")
    elif letra=="i":
        print("la letra ",letra,"Es vocal")
    elif letra=="o":
        print("la letra ",letra,"Es vocal")
    elif letra=="u":
        print("la letra ",letra,"Es vocal")
else:
    print("No se puede procesar el dato")