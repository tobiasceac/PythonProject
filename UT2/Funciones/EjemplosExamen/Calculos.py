import math


def areaCirculo(r):
    return math.pi * r**2

def areaCuadrado(lado):
    return lado**2

def areaTriangulo(base = 8, alto = 15):
    return base * alto / 2

def precioEntrada(edad, estudiante= False, precio_normal= 10):
    if edad < 18 or estudiante:
        return precio_normal * 0.5
    return precio_normal

def multiplicandoUnaSuma(*args, multiplicador = 1):
    return sum(args) * multiplicador

def contarArgumentos(*args):
    return sum(args)

def filtrarPares(lista_numeros):
    return [num for num in lista_numeros if num % 2 == 0]
