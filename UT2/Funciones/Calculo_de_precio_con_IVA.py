def calcular_precio(precio_base: float, iva: float = 21):
    ivaProd = precio_base * (iva / 100)
    resultado = precio_base + ivaProd
    return resultado

print(calcular_precio(10))