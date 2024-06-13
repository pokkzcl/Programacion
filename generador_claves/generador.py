import os
import pickle
import string
import random
import platform

contador = 0
# Leer numero de claves generadas desde el archivo
def leer():
    global contador
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, 'contador.pkl')
        with open(file_path, 'rb') as archivo:
            contador = pickle.load(archivo)
            if contador == 0:
                print("No se han generado claves aun.")
    except Exception as e:
        return

# Guardar numero de claves generadas
def guardar(contador):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'contador.pkl')
    with open(file_path, 'wb') as archivo:
        pickle.dump(contador, archivo)

# Preguntar al usuario -> parametros (largo)
def definir_clave():
    try: 
        largo = input("Largo de clave a generar: ")
        largo = int(largo)
        return largo
    except Exception as e:
        print(e)

# Generador principal
def generador(largo):
    
    # crear listado de caracteres usando STRING
    caracteres = string.ascii_letters + string.digits + string.punctuation
    clave = ''.join(random.choice(caracteres) for i in range(largo))

    return clave


# Funcion Main
def main():
    global contador
    # Limpiar pantalla
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    
    # Leer contador (archivo)
    leer()

    # Mostrar mensaje de bienvenida
    print("--- Generador de claves ---\n")
    print(f"Se han generado {contador} claves con este programa.\n")

    print("1. Generar clave")
    print("2. Volver al menu principal\n")

    try:
        opcion = int(input("\nOpcion: "))
        if opcion == 1:
            os.system('cls' if platform.system() == 'Windows' else 'clear')

            # Generar clave
            largo = definir_clave()
            print(generador(largo))
            input("Presione ENTER para continuar...")
            # Incrementar contador
            contador += 1

            # Guardar contador
            guardar(contador)
            
        if opcion == 2:
            return
    except Exception as e:
        print(e)
        main()
        
    main()
    

    

# Correr funcion solo si se corre desde el archivo mismo.
if __name__ == '__main__':
    main()
    


