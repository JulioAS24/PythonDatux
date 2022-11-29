#10.Realizar un programa que calcule la penalidad por la mora
#  de una deuda,sabiendo que si se demora de 1 día a 10 se le 
# agrega el 5% , si se demora hasta 30 días se le agrega 8% y pasando el rango máximo se le agrega un 10%

t=0.0
monto=1000
dia=int(input("Ingrese los días de demora: "))

if dia>=1 and dia<=10:
    t=0.05
    print("Se le agrega un 5%: ",t)
elif dia<=30:
    t=0.08
    print("Se le agrega un 8%: ",t)
else:
    t=0.10
    print("Se le agrega un 10%: ",t)

