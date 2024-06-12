from .mascota import Mascota
import pickle
import os

mascotas = []

def cargar_mascotas():
    global mascotas
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'mascotas.pkl')
    try:
        with open(file_path, "rb") as file:
            mascotas = pickle.load(file)
    except Exception as e:
        print(e)
        print("No se pudo cargar las mascotas.")

def guardar_mascotas():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'mascotas.pkl')
    with open(file_path, "wb") as file:
        pickle.dump(mascotas, file)

def mostrar_mascotas():
    if len(mascotas) == 0:
        os.system(f"cls" if os.name == "nt" else "clear")
        print("Ninguna mascota registrada :c")
        input("\nEnter para continuar...")
    else:
        os.system(f"cls" if os.name == "nt" else "clear")
        for mascota in mascotas:
            print(mascota)
        input("\nEnter para continuar...")

def agregar_mascota():
    os.system(f"cls" if os.name == "nt" else "clear")
    dueño = input("Nombre del dueño: ")
    tipo = input("Tipo de mascota: ")
    nombre = input("Nombre de la mascota: ")

    mascota = Mascota(nombre, tipo, dueño)
    mascotas.append(mascota)
    guardar_mascotas()

def eliminar_mascota():
    nombre = input("Nombre de la mascota a eliminar: ")

    for i, mascota in enumerate(mascotas):
        if mascota.nombre == nombre:
            del mascotas[i]
            print(f"Mascota {nombre} eliminada.")
            return

    print(f"No se encontró ninguna mascota con el nombre {nombre}.")

def veterinaria():
    os.system(f"cls" if os.name == "nt" else "clear")
    cargar_mascotas()
    print("--- Veterinaria ---\n")
    opciones = [". Lista Mascotas",". Agregar mascota", ". Eliminar mascota", ". Volver al menu"]

    for i, opcion in enumerate(opciones):
        print(f"{i+1}{opcion}")

    try:
        opcion = input("\nIngrese su opción: ").strip()
        opcion = int(opcion)

        if opcion == 1:
            mostrar_mascotas()
        elif opcion == 2:
            agregar_mascota()
        elif opcion == 3:
            eliminar_mascota()
        else:
            print("Saliendo de la veterinaria...")
            input("Enter para continuar...")
            return

    except Exception as e:
        print(e)

    veterinaria()


