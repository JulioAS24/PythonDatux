#8.Escribir un programa que almacene la cadena de caracteres contraseña en
#  una variable, pregunte al usuario por la contraseña e imprima por 
# pantalla si la contraseña introducida por el usuario coincide
#  con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

var="contraseña"
print("Escriba la contraseña")
usuario=input("Introduzca la contraseña: ")
if usuario == var:
    print("La contraseña es correcta")
else:
    print("La Contraseña es incorrecta")
    print("Vuelva a escribir la contraseña")
