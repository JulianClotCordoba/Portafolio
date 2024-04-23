# Julian Clot Cordoba
# Universidad Fidelitas
# Integracion de conocimientos 2
# Programacion basica

admin1 = "juan-romero"
cedula1 = "109858663"

admin2 = "sofia-tames"
cedula2 = "30652745"

citas = []

def ingresar():
    usuario = input("Digite el nombre con el apellido del administrador, juntelos con un guion(-) y todo en minuscula sin tildes: ")
    cedula = input("Digite la cedula del administrador: ")
    if (usuario == admin1 or usuario == admin2) and (cedula == cedula1 or cedula == cedula2):
        print("El usuario ha iniciado sesion exitosamente!")
        while True:
            print("1. Mostrar informacion de las citas.")
            print("2. Crear cita")
            print("3. Salir")
            opcion = int(input("Que opcion quieres elegir? "))
            if opcion == 1:
                if citas:
                    print("A continuacion estan las citas del dia de hoy: ")
                    for i in range(0, len(citas), 4):
                        print("Fecha:", citas[i], "Hora:", citas[i + 1], "Paciente:", citas[i + 2], "Estado:", citas[i+3])
                else:
                    print("No existe ninguna cita agendada para el dia de hoy")
            elif opcion == 2:
                fecha_general = input("Introduce la fecha general formato (-/-/-): ")
                citas.append(fecha_general)
                hora_de_cita = input("Introduce la hora de la cita en formato: ")
                citas.append(hora_de_cita)
                paciente = input("Introduzca el nombre del paciente: ")
                citas.append(paciente)
                activado = input("Introduzca el estado de la cita (True, False): ")
                citas.append(activado)
                print("La cita se creo!")
            elif opcion == 3:
                break
    else:
        print("El usuario no existe, por favor vuela a iniciar sesion. ")

while True:
    print("1. Ingresar")
    print("2. Salir")
    opcion = int(input("Que opcion quieres elegir? "))

    if opcion == 1:
        ingresar()
    elif opcion == 2:
        break

