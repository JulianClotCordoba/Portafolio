# Julian Clot Cordoba
# Universidad Fidelitas
# Porgramacion Basica


with open("personas.txt", "w") as personas_data:
    pass

personas_ing = []
personas_eg = []

def ingresar():
    cantidad_de_personas_ingresadas = input("Cual es tu nombre para ingresarte ")
    personas_ing.append(cantidad_de_personas_ingresadas)
    if len(personas_ing) <= 10:
        with open("personas.txt", "a") as personas_data:
            personas_data.write("\n" + cantidad_de_personas_ingresadas + "\n")
    else:
        print("La cantidad de personas supero el maximo de capacidad.")

def egresar():
    cantidad_de_personas_egresadas = input("Cual es tu nombre para egresarte ")
    if cantidad_de_personas_egresadas in personas_ing:
        personas_ing.remove(cantidad_de_personas_egresadas)
        with open("personas.txt", 'r+') as per:
            contenido = per.read()
            contenido_modificado = contenido.replace(cantidad_de_personas_egresadas, '')
            per.seek(0)
            per.write(contenido_modificado)
            per.truncate()
        print(f"{cantidad_de_personas_egresadas} ha salido correctamente.")
    else:
        print(f"{cantidad_de_personas_egresadas} no se encuentra en la lista de ingresados.")

while True:
    print("1. Ingresar")
    print("2. Egresar")
    print("3. Salir")
    opcion = input("Que opciion quieres elegir ")

    if opcion == "1":
        ingresar()
    elif opcion == "2":
        egresar()
    elif opcion == "3":
        break
