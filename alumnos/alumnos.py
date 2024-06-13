# almancenar alumnos, nombre, curso, promedio final
# 1. Ingresar alumnos
# 2. Mostrar alumnos (mostrar promedio general)
# 3. Mostrar alumnos por curso y promedio curso
# 4. Salir

import pickle
import os
import platform

alumnos = []

def guardar_archivo():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'alumnos.pkl')
    with open(file_path, "wb") as file:
        pickle.dump(alumnos, file)
        
def leer_archivo():
    global alumnos
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'alumnos.pkl')
    try:
        with open(file_path, "rb") as file:
            alumnos = pickle.load(file)
    except Exception as e:
        print(e)
        print("No se pudieron cargar los alumnos.")



def ingresar_alumno():
    alumno = {}

    alumno['Nombre'] = input("Ingrese el nombre del alumno: ").strip().lower()
    alumno['Curso'] = input("Ingrese el curso de alumno: ").strip().lower()
    alumno['Promedio'] = input("Ingrese el promedio: ").strip().lower()
    alumnos.append(alumno)

    guardar_archivo()


def mostar_alumnos(): 
    promedioAlumnos = 0
    totalAlumnos = len(alumnos)

    os.system(f"cls" if platform.system() == "Windows" else "clear") # se cambio por platform.system() == 'Windows'

    for alumno in alumnos:
        p = alumno['Promedio']
        promedioAlumnos += int(p) # se modifico p a int(p)
        print(f"Nombre: {alumno['Nombre']}")
        print(f"Curso: {alumno['Curso']}")
        print(f"Promedio: {alumno['Promedio']}")
        
        
        
    promedio = promedioAlumnos / totalAlumnos
    print(f"\nEl promedio del curso es: {promedio}")
    input("Enter para continuar...")

def mostar_curso():
    pass

def main():
    leer_archivo()
    os.system(f"cls" if platform.system() == 'Windows' else 'clear') # se cambio por platform.system() == 'Windows'

    opciones = [". Ingresar alumno", ". Mostrar alumnos", ". Mostrar alumnos por curso", ". Volver al menu"]
    
    for i, opcion in enumerate(opciones):
        print(f"{i+1}{opcion}")
    
    try:
        opcion = int(input("\nIngrese su opcion: "))

        if opcion == 1:
            ingresar_alumno()
        elif opcion == 2:
            mostar_alumnos()
        else:
            return

    except Exception as e:
        print(e)

    main()


if __name__ == '__main__':
    main()

