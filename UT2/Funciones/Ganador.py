import random


def ganador(*participantes: str):
    if len(participantes) == 0:
        return "No hay participantes"
    return random.choice(participantes)


print(ganador("Hola", "Pepe", "Pedro", "Jose"))