def saludar(nombre):
    return f"Hola {nombre}"

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def ejemplo(**kwargs):
    print(kwargs)
