def saludoPersonalizado(nombre: str, saludo: str = "Hola"):
    return f"{saludo}, {nombre}"

print(saludoPersonalizado("Pedro", "Adios"))
