def mostrar_menu():
    print("\nAGENDA\n")
    print("1. Nuevo contacto.")
    print("2. Eliminar contacto.")
    print("3. Buscar contacto.")
    print("4. Lista contactos.")
    print("0. Salir.")

def agregar_contacto(agenda):
    nombre = input("Nombre? ")
    telefono = input("Tel.? ")
    email = input("email? ")
    agenda[nombre] = { "telefono": telefono, "email": email }
    print(f"Contacto {nombre} agregado!")

def eliminar_contacto(agenda):
    nombre = input("Nombre? ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"Contacto {nombre} no existe.")

def buscar_contacto(agenda):
    nombre = input("Nombre a buscar? ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"Contacto {nombre} no encontrado.")

def listar_contactos(agenda):
    if agenda:
        print("\nLista contactos:")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Tel.: {info['telefono']}")
            print(f"Email: {info['email']}")
            print("-" * 20)
    else:
        print("Agenda vacía.")

def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("? ")
        if opcion == "0":
            print("Adios...")
            break
        elif opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda) 
        else:
            print("Error.")


agenda_contactos()