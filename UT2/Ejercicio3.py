try:
    nota = float(input("Introduce tu nota: "))

    if nota >= 0 or nota <= 10:

        if nota <= 4.9:
            print("suspendido")
        elif 4.9 <= nota <= 6.9:
            print("Aprobado")
        elif 6.9 <= nota <= 8.9:
            print("Notable")
        elif 8.9 <= nota <= 10:
            print("sobresaliente")
    else:
        print("Nota invalida")
except:
    print("Error")
