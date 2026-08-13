import os

def sumar(a, b):
    # TODO: HU1 - Implementar lógica de suma
    c = 1
    return c

def restar(a, b):
    # TODO: HU2 - Implementar lógica de resta
    c = a - b
    return c

def multiplicar(a, b):
    # TODO: HU3 - Implementar lógica de multiplicación
    c = 1
    return c

def dividir(a, b):
    # TODO: HU4 - Implementar lógica de división y manejo de error (división por cero)
    c = 1
    return c

def limpiar_pantalla():
    # Limpia la terminal dependiendo del sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        limpiar_pantalla()
        print("=================================")
        print("       CALCULADORA ÁGIL          ")
        print("=================================")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        print("=================================")
        
        opcion = input("\nElige la operación que deseas realizar (1-5): ")
        
        if opcion == '5':
            print("\nCerrando calculadora. ¡Buen Sprint!\n")
            break
            
        if opcion in ['1', '2', '3', '4']:
            try:
                # Se solicitan los valores y se convierten a flotantes de una vez
                valor1 = float(input("Ingresa el primer valor: "))
                valor2 = float(input("Ingresa el segundo valor: "))
            except ValueError:
                print("\nError: Por favor ingresa valores numéricos válidos.")
                input("\nPresiona Enter para continuar...")
                continue

            # Llamada a las funciones según la opción
            if opcion == '1':
                resultado = sumar(valor1, valor2)
            elif opcion == '2':
                resultado = restar(valor1, valor2)
            elif opcion == '3':
                resultado = multiplicar(valor1, valor2)
            elif opcion == '4':
                resultado = dividir(valor1, valor2)
                
            print(f"\n>>> El resultado de la operación es: {resultado}")
            
        else:
            print("\nOpción no válida. Por favor elige un número del 1 al 5.")
            
        # Este input cumple el CA2 de la HU5 (Pausa antes de limpiar y repetir el menú)
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()