def calculo_inversion(inversion, interesAnual, years):

    for i in range(0, years):
        resultado = inversion * (interesAnual / 100)
        inversion += resultado
        return
        print(f"Total del año {i + 1}: {resultado + inversion}")


inversion = float(input("Inversion: "))
interesAnual = float(input("Interes: "))
years = int(input("Years: "))

calculo_inversion(inversion, interesAnual, years)