# Tarea 15 - Colecciones de datos
# Registro sencillo de clientes de un despacho jurídico

clientes = {}

def agregar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    telefono = input("Ingrese el número de teléfono: ")
    tramite = input("Ingrese el tipo de trámite: ")

    clientes[nombre] = {
        "telefono": telefono,
        "tramite": tramite
    }

    print("Cliente registrado correctamente.\n")


def mostrar_clientes():
    if not clientes:
        print("No existen clientes registrados.\n")
        return

    print("\n--- CLIENTES REGISTRADOS ---")

    for nombre, datos in clientes.items():
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {datos['telefono']}")
        print(f"Trámite: {datos['tramite']}")
        print("----------------------------")


def buscar_cliente():
    nombre = input("Ingrese el nombre del cliente que desea buscar: ")

    if nombre in clientes:
        print("\nCliente encontrado:")
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {clientes[nombre]['telefono']}")
        print(f"Trámite: {clientes[nombre]['tramite']}\n")
    else:
        print("Cliente no encontrado.\n")


def eliminar_cliente():
    nombre = input("Ingrese el nombre del cliente que desea eliminar: ")

    if nombre in clientes:
        del clientes[nombre]
        print("Cliente eliminado correctamente.\n")
    else:
        print("Cliente no encontrado.\n")


while True:
    print("\n===== REGISTRO DE CLIENTES =====")
    print("1. Agregar cliente")
    print("2. Mostrar clientes")
    print("3. Buscar cliente")
    print("4. Eliminar cliente")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_cliente()

    elif opcion == "2":
        mostrar_clientes()

    elif opcion == "3":
        buscar_cliente()

    elif opcion == "4":
        eliminar_cliente()

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")