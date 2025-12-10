# Reemplaza cada palabra con la primera letra en mayuscula y cuenta cuantas 'e' hay.
# frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"


def reemplaza_cuenta(frase, letra):
    return f"{frase.title()}\n{frase.count(letra)} veces aparece la letra {letra}"


print(reemplaza_cuenta(frase, "e"))
