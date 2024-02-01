#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS
#Y PRECIOS DE LA TABLA, DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO
#Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA EL PRECIO TOTAL. SI
#EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO

#--------------Ejercicio de clase-----------

diccionario={"Mango" : 5000,
             "Fresa" : 2000, 
             "Lulo" : 6000
             }

for llave,valor in diccionario.items():
    print(llave,valor)

producto=str( input("ingrese el producto a comprar: "))
producto = producto.capitalize()
peso=int(input("ingrese la cantidad  de libras a comprar "))

variableBusqueda=diccionario[producto]

total=variableBusqueda*peso
print(f" valor total del producto {producto} sera de:{total}")

#creaado por -----
#Helen Nataly Parga Murillo