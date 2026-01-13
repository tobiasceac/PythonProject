base = 2

guerrero = {
    "vida": base * 2,
    "defensa": base * 2,
    "ataque":  2,
    "alcance": 2,
}

caballero = {
    "vida": guerrero.get("vida") * 2,
    "defensa": guerrero.get("defensa") * 2,
    "ataque": base,
    "alcance": base
}

guerrero.update({"ataque": caballero.get("ataque") * 2})
guerrero.update({"alcance": caballero.get("ataque") * 2})

arquero = {
    "vida": guerrero.get("vida"),
    "defensa": guerrero.get("defensa") / 2,
    "ataque": guerrero.get("ataque"),
    "alcance": guerrero.get("alcance") * 2,
}

print("Guerrero", guerrero, "Caballero", caballero, "Arquero", arquero)