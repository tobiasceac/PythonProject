from random import Random

while True:
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")


    opcion = input("\nSelecciona una operación (1-5): ").strip()

    if opcion == '5':
        print("\n👋 ¡Gracias por usar la calculadora! Hasta pronto.")
        break

    if opcion not in ['1', '2', '3', '4']:
        print("Error: Opcion no valida, selecciona entre 1 y 5.")
        continue

    try:
        num1 = float(input("Primer número: "))
        num2 = float(input("Segundo número: "))

        if opcion == '1':
            resultado = num1 + num2
            operador = "+"
        elif opcion == '2':
            resultado = num1 - num2
            operador = "-"
        elif opcion == '3':
            resultado = num1 * num2
            operador = "×"
        elif opcion == '4':
            resultado = num1 / num2
            operador = "÷"

        print(f"\n Resultado: {num1} {operador} {num2} = {resultado}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"\n Error: {e}")

