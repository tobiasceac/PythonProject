try:
    Horas = float(input("introduce las horas: "))
    Rate = float(input("introduce el precio de la hora: "))
except:
    Horas = -1
    Rate = -1

if Horas > 0 or Rate > 0:
    print("bien")
else:
    print("Error")

if Horas > 40:
    Extra = (Horas - 40) * (Rate * 1.5)
    Pay = 40 * Rate + Extra
else:
    Pay = Horas * Rate

