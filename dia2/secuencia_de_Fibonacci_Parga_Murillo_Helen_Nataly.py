def fibonacci(n):
    fib_sequence = [0, 1]
    i = 2

    while i < n:
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        i += 1

    return fib_sequence

if __name__ == "__main__":
    print("¡Bienvenido al generador de la Secuencia de Fibonacci!")
    print("La Secuencia de Fibonacci comienza con 0 y 1, y cada término subsiguiente es la suma de los dos términos anteriores.")

    while True:
        try:
            n = int(input("\nIngrese un valor entero 'n' para generar la secuencia (o ingrese 0 para salir): "))
            
            if n == 0:
                print("¡Hasta luego! Gracias por usar el generador de Fibonacci.")
                break
            elif n < 0:
                print("Por favor, ingrese un valor entero no negativo.")
                continue

            fib_result = fibonacci(n)
            print(f"Secuencia de Fibonacci hasta el término {n}: {fib_result}")

        except ValueError:
            print("Por favor, ingrese un valor entero válido.")