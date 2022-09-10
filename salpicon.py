# 2.Leer el nombre de 10 frutas {nombre, color, precio} para preparar un
# salpicón; el programa debe permitir mostrar las 10 frutas ingresadas al
# mismo tiempo en sentido inverso al ingresado+(1)

cantidadDeFrutas =int(input('Cuantas frutas quiere ingresar? '))
lista=[]


for cantidad in range(cantidadDeFrutas):

    diccionario={}

    diccionario['Nombre']=input('Nombre de fruta ')
    diccionario['Color']=input('Color de fruta ')
    diccionario['Precio']=input('Precio de fruta ')
    lista.reverse()
    lista.append(diccionario)

print(lista)

listaReverse=len(lista)

for i in range(cantidadDeFrutas):
    print(lista[listaReverse-1])
    listaReverse-=1



