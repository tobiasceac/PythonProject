
cEuros = float(input("Introduce la cantidad de euros: "))
divisa = input("Introduce la divida: ").upper()

USD = 1.17
GBP = 0.85
JPY = 176.08

try:
    if cEuros <= 0:
        raise ValueError("El numero debe ser positivo")
    if divisa == "USD":
        cambio = cEuros * USD
    elif divisa == "GBP":
        cambio = cEuros * GBP
    elif divisa == "JPY":
        cambio = cEuros * JPY
    else:
        raise ValueError("Divisa no valida")
    print("El resultado es: ", cambio)

except ValueError as e:
    print("Error ", e)