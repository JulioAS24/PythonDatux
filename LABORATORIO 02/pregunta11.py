#11.Definir los atributos y métodos de una de las siguientes clases.
#- Persona
#- Gato
#- Producto


#---TOMAREMOS PERSONA::

 
class Persona:
    nBrazos=0
    nPiernas=0
    cabello=True
    cCabello="Defecto"
    hambre=0
    def __init__(self) :
        self.nBrazos=2
        self.nPiernas=2
    def dormir():
        pass
    def comer(self):
        self.hambre=1

class Hombre(Persona):
    nombre="Defecto"
    sexo="M"
    def cambiarNombre(self,nombre):
        self.nombre=nombre

class Mujer(Persona):
    nombre="Defecto"
    sexo="F"

Valera=Hombre()
Valera.comer()
print(Valera.hambre)
##VALERA PORQUEEEEEEEEEEEEEEEEEEEEEEEEEEE

