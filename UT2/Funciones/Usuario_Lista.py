usuarios = []

def crear_usuario(nombre: str, email: str, activo: bool = True):

    usuario = [nombre, email, activo]
    usuarios.append(usuario)

    activos = [u for u in usuarios if u[2] == True]

    print("Usuarios activos:")
    for u in activos:
        print(u)

crear_usuario("a", "b")
crear_usuario("a", "cha", False)
crear_usuario("hol", "bas", True)