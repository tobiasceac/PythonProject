
print("Menu")
print("1. Perfil")
print("2. Editar Perfil")
print("3. Salir")
try:

    opcion = int(input("Ingrese la opcion: "))

    while opcion != 3:
        match opcion:
            case 1:
                print("Perfil")
            case 2:
                print("Editar Perfil")
            case _:
                print("error")
        opcion = int(input("Ingrese la opcion: "))
except:
    print("error")