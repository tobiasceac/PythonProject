numeros = []

for i in range (5):
    num = int(input("Introduce um numero: "))
    numeros.append(num)

for i in range(len(numeros) - 1):
    for j in range(len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Números ordenados de menor a mayor:")
print(numeros)


numeros.sort()
print(numeros)


