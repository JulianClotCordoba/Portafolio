# Grupo #1
# Programacion basica
# Universidad Fidelitas

usuarios = []
contrasenas = []
inventario = {}

usuario_registro = input("Ingrese su usuario: ")
contrasena_registro = input("Ingrese su contraseña: ")

usuarios.append(usuario_registro)
contrasenas.append(contrasena_registro)

print("*******************************************************")

while True:
    opcion = input(" ¿Desea ingresar al sistema? (Sí/No): ").lower()
    if opcion != "si":
        print("Saliendo del programa.")
        break

    for intento in range(3):
        usuario_ingreso = input("Ingrese su usuario: ")
        contrasena_ingreso = input("Ingrese su contraseña: ")

        if usuario_ingreso in usuarios and contrasena_ingreso == contrasenas[usuarios.index(usuario_ingreso)]:
            print("Inicio de sesión exitoso. Bienvenido")

            while True:
                print("1. Agregar vehichulo")
                print("2. Inhabilitar vehiculo")
                print("3. Realizar reserva")
                print("4. Salir")
                menu = input("Eliga la opcion que desea: ")

                if menu == "1":
                    placa = input("Ingrese la placa del vehiculo: ")
                    if placa in inventario:
                        print("Ya existe un vehiculo con esa placa.")
                    else:
                        marca = input("Ingrese la marca del vehículo: ")
                        año = input("Ingrese el año del vehículo: ")
                        modelo = input("Ingrese el modelo del vehículo: ")
                        cilindraje = input("Ingrese el cilindraje del vehículo: ")
                        precio_alquiler = float(input("Ingrese el precio de alquiler por día del vehículo: "))
                        precio_vehiculo = float(input("Ingrese el precio del vehículo: "))
                        cantidad = int(input("Ingrese la cantidad de este vehículo: "))
                        inventario[placa] = {"Marca": marca, "Año": año, "Modelo": modelo, "Cilindraje": cilindraje,
                                             "Precio Alquiler": precio_alquiler, "Precio Vehículo": precio_vehiculo,
                                             "Cantidad": cantidad}
                        print("Vehiculo agregado exitosamente.")
                elif menu == "2":
                    placa = input("Ingrese la placa del vehiculo: ")
                    if placa not in inventario:
                        print("No existe un vehiculo con esa placa.")
                    else:
                        del inventario[placa]
                        print("Vehiculo inhabilitado exitosamente.")
                elif menu == "3":
                    marca = input("Ingrese la marca del vehiculo que desea reservar: ")
                    año = input("Ingrese el año del vehiculo que desea reservar: ")
                    modelo = input("Ingrese el modelo del vehiculo que desea reservar: ")
                    if marca in inventario and año in inventario and modelo in inventario and inventario[modelo]["Cantidad"] > 0:
                        inventario[modelo]["Cantidad"] -= 1
                        print("Reserva realizada con exito.")
                    else:
                        print("No hay espacios disponibles para reservar ese modelo.")
                elif menu == "4":
                    print("Saliendo al menu principal.")
                    break
                else:
                    print("Error, porfavor vuelva a intentar.")
            break
        else:
            print("Error en el usuario o contraseña. Intentos restantes:", 2 - intento)
            if intento == 2:
                print("Se agotaron los intentos. Volviendo al menú principal.")
                break
