import pickle
import os 

# Importar modulos
from vet.veterinaria import *
from promedio.promedio import *

def menu():
    os.system(f"cls" if os.name == "nt" else "clear")
    print("--- Menu ---\n")

    opciones = [". Promedio", ". Veterinaria", ". Salir"]

    for i, opcion in enumerate(opciones):
        print(f"{i+1}{opcion}")
    
    try:
        opcion = input("\nIngrese su opción: ").strip()
        opcion = int(opcion)

        if opcion == 1:
            calculadora_promedio()
        elif opcion == 2:
            veterinaria()
        else:
            exit()

    except Exception as e:
        print(e)
    
    menu()

def main():
    menu()

if __name__ == "__main__":
    print(dir(veterinaria))