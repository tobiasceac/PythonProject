# Ordenar por longitud de la palabra de menor a mayor

def longitud(palabra):
    return len(palabra)

palabras = ["a", "Hola", "HolaMundo", "Tigre", "Sol", "b"]

palabras_ordenadas = sorted(palabras, key=longitud)
print(palabras_ordenadas)

# Ordenar de pares a impares

def parImpar(num):
    return num % 2

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_ordenadas = sorted(numeros, key=parImpar)
print(numeros_ordenadas)