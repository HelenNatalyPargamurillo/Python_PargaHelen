def min_coins(denominaciones, monto):
    # Inicializar el número total de monedas a cero
    num_monedas = 0
    
    # Ordenar las denominaciones de monedas de mayor a menor
    denominaciones.sort(reverse=True)
    
    # Iterar sobre las denominaciones
    for denom in denominaciones:
        # Calcular cuántas monedas de esta denominación se pueden utilizar
        num_monedas += monto // denom
        
        # Actualizar el monto restante
        monto %= denom
    
    # Verificar si se puede cambiar completamente el monto
    if monto == 0:
        return num_monedas
    else:
        return -1  # No se puede cambiar completamente con las denominaciones dadas

# Ejemplo de uso
denominaciones = [1, 5, 10]
monto_objetivo = int(input("Ingrese el monto: "))

resultado = min_coins(denominaciones, monto_objetivo)

if resultado != -1:
    print(f"El número mínimo de monedas para cambiar {monto_objetivo} es: {resultado}")
else:
    print(f"No es posible cambiar {monto_objetivo} con las denominaciones dadas.")
