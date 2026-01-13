import math

# Ejercicio 1
def calcular_estadisticas(*numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    media = sum(numeros) / len(numeros)

    estadisticas = (minimo, maximo, media)
    return estadisticas

# Ejercicio 2
def distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Ejercicio 3
def analizar_texto(texto: str):
    nCaracteres = len(texto)
    palabras = texto.split()
    nPalabras = len(palabras)
    pPalabras = palabras[0]

    analisis = (nCaracteres, nPalabras, pPalabras)
    return analisis

# Ejercicio 4
def convertir_temperatura(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15

    temperatura = (fahrenheit, kelvin)
    return temperatura

# Ejercicio 5
def analizar_numeros(numeros):
    pares = 0
    impares = 0
    suma = 0

    for n in numeros:
        suma += n
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    analisis = (pares, impares, suma)
    return analisis

# Ejercicio 6
def procesar_cadena(cadena):
    mayusculas = cadena.upper()
    minusculas = cadena.lower()
    longitud = len(cadena)

    procesado = (mayusculas, minusculas, longitud)
    return procesado