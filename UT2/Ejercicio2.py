try:
    num1 = float(input("introduce el primer numero: "))
    num2 = float(input("introduce el segundo numero: "))

    if num1 > num2:
        print("num1 es mayor")
    elif num1 < num2:
        print("num2 es mayor")
    else:
        print("Son iguales")
except:
    print("Error")