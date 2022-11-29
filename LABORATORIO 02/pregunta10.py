#10.Realizar un programa que realice las siguientes funciones de string al texto.
#-split
#-count
#-find
#-uppercase
#-lowercase
#texto=”Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
#Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
#impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y
#los mezcló de tal manera que logró hacer un libro de textos especimen.”

#Uso del método str.split()
textos12="Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen."
y=textos12.split(" ")
print(f"2:{y}")

#Uso del método str.count()
#---numero de veces que se repite 
for i in textos12:
    print(i,"=",textos12.count(i),"veces")


#Uso  del método str.find()
indice=textos12.find('texto')
print(indice)

#-Uso del método str.uppercase()
#---todo a mayúsculas
print(textos12.upper())

#-Uso del método str.lowercase()
#---todo a minúsculas
print(textos12.lower()) 

