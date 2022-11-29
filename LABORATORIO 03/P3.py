
#3.Crear una clase Animal, luego una clase Perro y gato que sean hijos de Animal,el método
# de Sonido debe ser diferente


def pregunta3():
    class animal:
        def __init__(self,sexo):
            self.sexo=sexo
        def __str__(self):
            pass
    class perro(animal):
        def sonianimal(self,sonido):
            print("El sonido del perro :",sonido)
    class gato(animal):
        def sonianimal(self,sonido):
            print("El sonido del gato :",sonido)
    mascota1=perro('macho')
    mascota2=gato('hembra')
    print("El sexo de mascota 1 es: ",mascota1.sexo)
    print("El sexo de mascota 2 es: ",mascota2.sexo)
    mascota1.sonianimal("guau")
    mascota2.sonianimal("miau")
