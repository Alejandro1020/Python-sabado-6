# 3.Construir un programa para ir de compras en un supermercado
# que permita la construcción del siguiente MENU:
# 1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
# 2. Digitar 2 para mostrar todos los productos registrados (+0.4)
# 3. Digitar 3 para permitir buscar por código un producto y editar el precio
# de este (+0.4)
# 4. Digitar 4 para permitir buscar por código un producto y eliminar el
# producto (+0.4)
# 5. Digitar 0 para SALIR

print("**MENU**")
print("1 para recibir un producto")
print("2 para mostrar todos los productos registrados")
print("3 para editar el precio producto")
print("4 para eliminar el producto")
print("5 para SALIR")

productos=[]

opt = 100

while( opt != 5 ):

    opt = int( input('Que desea elegir: ') )

    producto = {}

    if (opt == 1):
        producto['codigo'] = int(input('Digite el codigo del producto: '))
        producto['nombre'] = input('Digite el nombre del producto: ')
        producto['precio'] = float(input('Digite el precio del producto: '))
        productos.append( producto )

    elif( opt == 2 ):
        print(productos)
    elif (opt == 3):
        codigo = int( input('Digite el codigo del producto que desee buscar: ') )
    
        for prod in productos:
            if ( prod['codigo'] == codigo ):
                prod['precio'] = float( input('Digite el nuevo precio: ') )
                break
            else:
                print('Producto no encontrado')
    elif (opt == 4):
        codigo = int( input('Digite el codigo del producto que desee buscar: ') )
    
        for prod in productos:
            if ( prod['codigo'] == codigo ):
               productos.remove(prod)
               print('Producto eliminado')
               break
            else:
                print('Producto no encontrado')
    else:
        print("digite una opcion valida")