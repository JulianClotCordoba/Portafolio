# Julian Clot
# Universidad Fidelitas


def crear_archivo(nombre_archivo):
    archivo = open(nombre_archivo + ".txt", "w")
    print("El archivo se a creado!")
    archivo.close()


def agregar_informacion():
    nombre = input("¿Cual es el nombre del estudiante? ")
    grupo = input("¿Cual es el numero del grupo? ")
    nota = float(input("¿Cual es la nota del estudiante? "))
    nombre_archivo = input("¿Que nombre le quiere poner al archivo? ")
    crear_archivo(nombre_archivo)

    archivo = open(nombre_archivo + ".txt", "a")
    archivo.write("Nombre: " + nombre)
    archivo.write("\n")
    archivo.write("Grupo: " + grupo)
    archivo.write("\n")
    archivo.write("Nota: " + str(nota))
    print("La informacion se ha concretado finalmente!")
    archivo.close()

def mostrar_archivo():
    nombre_archivo = input("¿Cual es el nombre del archivo que quieres abrir? ")
    archivo = open(nombre_archivo + ".txt", "r")
    leer=archivo.read()
    print(leer)
    archivo.close()

while True:
    print("1. Agregar informacion ")
    print("2. Mostrar archivo ")
    print("3. Salir")
    menu = int(input("Eliga la opcion que desea: "))

    if menu == 1:
        agregar_informacion()
    elif menu == 2:
        mostrar_archivo()
    elif menu == 3:
        break
