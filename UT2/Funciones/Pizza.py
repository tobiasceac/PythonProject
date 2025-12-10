def make_pizzas(size: int, *ingredientes):
    if len(ingredientes) == 0:
        print("Pizza sin ingredientes")
    else:
        print(f"Has elegido una pizza de {size} porciones con estos ingredientes:")
        for ing in ingredientes:
            print(f" - {ing}")

make_pizzas(8)


