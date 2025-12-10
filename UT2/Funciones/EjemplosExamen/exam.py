def area_rectangulo(ancho, alto=1):
    if ancho < 0 or alto < 0:
        return None
    return ((ancho ** 2) * alto) / 2

def contar_atras(n):
    print(n)
    if n <= 0:
        return
    else:
        contar_atras(n-1)

contar_atras(5)


