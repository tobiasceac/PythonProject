inversion = float(input("Inversion: "))
interesAnual = float(input("Interes: "))
years = int(input("Years: "))

for i in range(0, years):
    resultado = inversion * (interesAnual / 100)
    inversion += resultado
    print(f"Total del año {i + 1}: {resultado + inversion}")
