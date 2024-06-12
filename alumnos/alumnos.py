# almancenar alumnos, nombre, curso, promedio final
# 1. Ingresar alumnos
# 2. Mostrar alumnos (mostrar promedio general)
# 3. Mostrar alumnos por curso y promedio curso
# 4. Salir

import pickle
import os

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

    os.system(f"cls" if os.system == "nt" else "clear")

    for alumno in alumnos:
        p = alumno['Promedio']
        promedioAlumnos += p
        print(f"Nombre: {alumno['Nombre']}")
        print(f"Curso: {alumno['Nombre']}")
        print(f"Promedio: {alumno['Promedio']}")
        
        
        
    promedio = promedioAlumnos / totalAlumnos
    print(f"\nEl promedio del curso es: {promedio}")
    input("Enter para continuar...")

def mostar_curso():
    pass

def main():
    leer_archivo()
    os.system(f"cls" if os.system == 'nt' else 'clear')

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


"""  import os
os.system("cls")

curso = []

while True:

  nombre = input("ingrese el nombre del alumno o 'salir': ").lower().strip()

  if nombre == "salir":
    break

  edad = input("ingrese edad del alumno: ")
  try:
    edad = int(edad)
  except ValueError:
    print("ingreso mal el dato, vuelva a intentarlo")
    continue
  print("coloque cada calificacion del alumno, una vez termino de colocar las calificaciones, ponga 'salir'")

  calificaciones = []
  while True:
    nota = input("Ingrese una nota o 'salir': ").lower().strip()

    if nota == "salir":
      break
    try:
      nota = float(nota)
    except:
      print("pusiste mal salir, o se te paso una letra")
      continue

    if nota < 1 or nota > 7:
      print("Numero fuera del rango")
      continue

    calificaciones.append(nota)

  try:
      promedio = sum(calificaciones) / len(calificaciones)

  except:
    print("Usted no agrego ningun valor")

  alumno = {
    "nombre": nombre,
    "edad": edad,
    "notas": calificaciones,
    "promedio": promedio
    }
  curso.append(alumno)

for alumno in curso:
    print("Nombre:", alumno["nombre"])
    print("Edad:", alumno["edad"])
    print("Calificaciones:", alumno["notas"])
    print("Promedio:", alumno["promedio"])
    print("\n") """