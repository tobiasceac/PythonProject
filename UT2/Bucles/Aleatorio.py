import random

def aleatorio():
    while True:
        try:
            aleatorio = random.randint(0, 100)
            print(f"Número aleatorio generado: {aleatorio}")

            numero = int(input("Introduce un número (0-100): "))

            if aleatorio == numero:
                print("¡Acertaste!")
                break
            else:
                print("No acertaste, intenta otra vez.")
        except ValueError as e:
            print("Error: debes introducir un número válido.")


aleatorio()




