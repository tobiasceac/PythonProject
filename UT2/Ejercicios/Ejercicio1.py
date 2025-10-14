try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        print("Introduce un valor positivo")
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
except ValueError:
    edad = -1
if edad < 0:
    print("ERROR: Introduce un numero positivo entero")


