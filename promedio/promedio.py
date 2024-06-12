# import os
import os

# Ponderaciones en porcentajes
formacion = [20, 35, 35, 10]
base_de_datos = [15, 30, 30, 25]
hw_y_sw = [15, 35, 30, 20]
programacion = [15, 25, 30, 30]
matematicas = [15, 25, 30, 30]

# Funciones
def ingresar_notas():
    os.system(f"cls" if os.name == "nt" else "clear")
    notas = []

    print("--- Ingresar Notas ---\n")
    try:
        for i in range(4):
            nota = input(f"Ingrese la nota {i+1}: ").strip()
            nota = float(nota)
            notas.append(nota)

        return notas
    except Exception as e:
        print(e)

def calcular_promedio(ponderacion, notas):
    os.system(f"cls" if os.name == "nt" else "clear")
    promedio = 0

    print("--- Calcular Promedio ---\n")
    try:
        for i in range(len(ponderacion)):
            promedio += ponderacion[i] * notas[i] / 100
        print(promedio)
    except Exception as e:
        print(e)

# Funcion Pric
def calculadora_promedio():
    while True:
        os.system(f"cls" if os.name == "nt" else "clear")

        # Menu
        print("--- Calculadora Promedios ---")

        opciones = [". Formeichon Ciudapapa", ". Batos de Dase", ". jarwer y softgüer", ". Seguramente programando en la paiton", ". numerosXletras", ". Volver al menú"]

        for i, opcion in enumerate(opciones):
            print(f"{i+1}{opcion}")

        try:
            opcion = input("\nIngrese su opción: ").strip()
            opcion = int(opcion)

            if opcion == 1:
                notas = ingresar_notas()
                calcular_promedio(formacion, notas)
                input("Enter para continuar...")
            elif opcion == 2:
                notas = ingresar_notas()
                calcular_promedio(base_de_datos, notas)
                input("Enter para continuar...")
            elif opcion == 3:
                notas = ingresar_notas()
                calcular_promedio(hw_y_sw, notas)
                input("Enter para continuar...")
            elif opcion == 4:
                notas = ingresar_notas()
                calcular_promedio(programacion, notas)
                input("Enter para continuar...")
            elif opcion == 5:
                notas = ingresar_notas()
                calcular_promedio(matematicas, notas)
                input("Enter para continuar...")
            else:
                break
        except Exception as e:
            print(e)

# Main
if __name__ == "__main__":
    calculadora_promedio()
            

    



