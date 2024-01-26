##---------------------------------------------------
##---- Ejercicio 1 -------
##----------------------------------------------------

## impresion en la consola
print("hola gente")



#_---------------datosprimitivos --
#1. sitring---
texto="campus"
print (texto)
print (type(texto))
2#_ int
numeroEntero=1
print(numeroEntero)
3# float
numeroDecimal=3.1
print (numeroDecimal)
#4 Double
(numerodecimalLargo)=3.141675748788545545541555488
print (numerodecimalLargo)
#5 booleen
booleano=True
print (booleano)
#------- Entradas parte delusuario con definicion de tipo de dato primitivo ----
entradaUsuario=input("ingresa tu nombre:")
print("tu nombre es", entradaUsuario)
#-----------Ciclos------------------ 
#1 ciclo for
for i  in range (5,10,2):
    print(i)

#2 ciclo while
    boleanito=True
    while boleanito == True: #while es lacondicion a cumplir
        print ("sigo vivo")
        boleanito = False

#-------------condicionales-------
    
texto1="campus"
if texto=="campus":
     print("soy campus")
else:
     print("nosoy campus")

#----------Funciones---------------
 
#1 con retorno con parametro
def retornar_superficie(lado):
    sup=lado*lado

    return sup

#2sin retorno con parametro
def calcular_cuadrado(numero):
    cuadrado = numero **2
    print("el cuadrado de",numero ,"es:",cuadrado)

#3 con retorno sin parametro
def obtener_numero():
    return 42

#4 sin retorno sin parametro  
    def saludo ():
         print ("saludo")
          

    

#-----------Areglos-------------
numeros_consecutivos = int        
numeros_consecutivos= [1,10]
for i in range(1.10):
    print(i)


## Desarollado por Helen Parga-1001301103