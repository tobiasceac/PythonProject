altura = int(input("Ingresa la altura de la piramide: "))


for i in range(1, altura + 1):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i)
    print(espacios + asteriscos)