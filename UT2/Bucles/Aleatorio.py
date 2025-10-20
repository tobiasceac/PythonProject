import random

while True:
    try:
        aleatorio = random.randint(0, 100)
        print(aleatorio)

        numero = int(input("Introduce un numero: "))

        if aleatorio == numero:
            print("Acertaste")
            break
        else:
            print("No acertaste")
    except ValueError as e:
        print(e)



