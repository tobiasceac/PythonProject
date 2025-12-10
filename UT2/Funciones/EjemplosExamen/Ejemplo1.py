import libreria
import exam

def sumar(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total
print(sumar(1, 2, 3, 4))  # 10

print(libreria.saludar("Tobias"))
print(libreria.factorial(10))
print(libreria.ejemplo(nombre = "tobias", edad = 18, hola = "1"))

print(exam.contar_atras(6))
