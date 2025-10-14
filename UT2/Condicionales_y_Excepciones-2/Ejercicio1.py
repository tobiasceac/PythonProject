try:
    num = int(input("Ingrese el numero: "))

    if num % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

    esPrimep = True

    for i in range(2, num):
        if num % i == 0:
            esPrimep = False
            break

    if esPrimep:
        print("Es primo")
    else:
        print("No es primo")

except:
    print("Error")