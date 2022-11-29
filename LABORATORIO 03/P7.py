
#7.Hacer un programa que consulte el valor del dolar (compra y venta) 
# de la fecha actual segun sunat (url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat')

def pregunta7():
    import requests
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)
    response.json() 
    data = response.json()
    compra = data['compra']
    venta = data['venta']
    fecha_actual = data['fecha']
    print("El valor del dólar en la compra es: ",compra)
    print("El valor del dólar en la venta es: ",venta)
    print("La fecha del cambio actual del dólar es: ",fecha_actual)
    print("Fin de ejecución")

