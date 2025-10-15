numero = int(input("Ingresa un numero: "))

divisor = 2
isPrimo = True

if numero <= 1:
    isPrimo = False
elif numero == 2:
    isPrimo = True

while divisor * divisor <= numero:
    if numero % divisor == 0:
        isPrimo = False
    divisor += 1

if isPrimo:
    print("Es primo")
else:
    print("No es primo")