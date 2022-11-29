#2. Una tienda de autopartes necesita un programa para catalogar sus productos,
# crear la clase Catálogo y producto realizar un objeto dentro de un catálogo productos el cual debe
#tener un método para agregar productos y otra para mostrar toda la lista de productos.


def pregunta2():
    class catalogo:
        productos=[]
        def __init__(self,productos=[]) :
            self.productos=productos
        def agregar(self,prod):
            self.productos.append(prod)
        def mostrar(self):
            for prod in self.productos:
                print(prod)            
    class producto:
        def __init__(self,nombre,cantidad):
            self.nombre=nombre
            self.cantidad=cantidad
            print('Se ha creado el producto:', self.nombre)
        def __str__(self):
            return ''.format() 
    
    prod=producto("TAMPICO",27)   
    c=catalogo([prod])
    c.mostrar()
    c.agregar(producto("CIFRUT",18))
    c.mostrar()

