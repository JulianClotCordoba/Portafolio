usuarios = []
contrasenas = []
cedula = []
inventario = {}
sedes = {
    "San Jose": "24 horas, los 7 días de la semana",
    "Alajuela": "24 horas, los 7 días de la semana",
    "Guanacaste": "Abren a las 4 am, cierran a las 11 pm.",
    "Limon": "Abren a las 6 am, cierran a las 10pm",
    "Puntarenas": "Abren a las 5 am, cierran a las 10 pm",
    "Perez Zeledon": "Abren a las 7 am, cierran a las 10 pm"
}

sede_actual = None

print("*******************************************************")

while True:
    if not sede_actual:
        print("Escoge una sede: ")
        for i, sede in enumerate(sedes.keys(), start=1):
            print(f"{i}. {sede} - Horario: {sedes[sede]}")
        opcion_ingreso = int(input("Elija una opción: "))
        sedes_disponibles = list(sedes.keys())
        if opcion_ingreso > 0 and opcion_ingreso <= len(sedes_disponibles):
            sede_actual = sedes_disponibles[opcion_ingreso - 1]
        else:
            print("Opción inválida, Intente de nuevo")
            continue
    print(f"Bienvenido a la sede {sede_actual}")
    while True:
        print("Menú de ingreso:")
        print("1. Usuario registrado")
        print("2. Nuevo usuario")
        print("3. Usuario invitado")
        print("4. Cambiar de sede")
        print("5. Salir")
        opcion_ingreso = input("Elija una opción: ")

        if opcion_ingreso == "1":
            for intento in range(3):
                usuario_ingreso = input("Ingrese su usuario: ")
                contrasena_ingreso = input("Ingrese su contraseña: ")

                if usuario_ingreso in usuarios and contrasena_ingreso == contrasenas[usuarios.index(usuario_ingreso)]:
                    print("Inicio de sesión exitoso. Bienvenido")

                    while True:
                        print("Menú de usuario registrado:")
                        print("1. Agregar vehículo")
                        print("2. Inhabilitar vehículo")
                        print("3. Realizar reserva")
                        print("4. Mostrar vehículos disponibles")
                        print("5. Salir")
                        menu = input("Elige la opción que deseas: ")

                        if menu == "1":
                            placa = input("Ingrese la placa del vehículo: ")
                            if placa in inventario:
                                print("Ya existe un vehículo con esa placa.")
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
                                print("Vehículo agregado exitosamente.")
                        elif menu == "2":
                            placa = input("Ingrese la placa del vehículo: ")
                            if placa not in inventario:
                                print("No existe un vehículo con esa placa.")
                            else:
                                del inventario[placa]
                                print("Vehículo inhabilitado exitosamente.")
                        elif menu == "3":
                            marca = input("Ingrese la marca del vehículo que desea reservar: ")
                            año = input("Ingrese el año del vehículo que desea reservar: ")
                            modelo = input("Ingrese el modelo del vehículo que desea reservar: ")

                            for placa, detalles in inventario.items():
                                if detalles["Marca"] == marca and detalles["Año"] == año and detalles["Modelo"] == modelo and detalles["Cantidad"] > 0:
                                    detalles["Cantidad"] -= 1
                                    print("Reserva realizada con éxito.")
                                    break
                            else:
                                print("No hay espacios disponibles para reservar ese modelo.")
                        elif menu == "4":
                            if inventario:
                                print("Vehículos disponibles: ")
                                for placa, detalles in inventario.items():
                                    print("Placa:", placa)
                                    print("Marca:", detalles["Marca"])
                                    print("Año:", detalles["Año"])
                                    print("Modelo:", detalles["Modelo"])
                                    print("------------------------")
                            else:
                                print("No hay vehículos disponibles.")
                        elif menu == "5":
                            print("Saliendo al menú de ingreso.")
                            break
                        else:
                            print("Error, por favor vuelve a intentar.")
                    break
                else:
                    print("Error en el usuario o contraseña. Intentos restantes:", 2 - intento)
                    if intento == 2:
                        print("Se agotaron los intentos. Volviendo al menú principal.")
                        break

        elif opcion_ingreso == "2":
            nuevo_usuario = input("Ingrese su nuevo usuario: ")
            nueva_contrasena = input("Ingrese su nueva contraseña: ")
            nueva_cedula = input("Ingrese su cedula: ")
            usuarios.append(nuevo_usuario)
            contrasenas.append(nueva_contrasena)
            cedula.append(nueva_cedula)
            inventario[nuevo_usuario] = {}
            print("Usuario registrado exitosamente.")

        elif opcion_ingreso == "3":
            print("Bienvenido, usted ingresó en modo invitado.")
            while True:
                print("Menú de usuario invitado:")
                print("1. Agregar vehículo")
                print("2. Inhabilitar vehículo")
                print("3. Mostrar vehículos disponibles")
                print("4. Salir")
                opcion_invitado = input("Elija una opción: ")

                if opcion_invitado == "1":
                    placa = input("Ingrese la placa del vehículo: ")
                    if placa in inventario:
                        print("Ya existe un vehículo con esa placa.")
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
                        print("Vehículo agregado exitosamente.")
                elif opcion_invitado == "2":
                    placa = input("Ingrese la placa del vehículo: ")
                    if placa not in inventario:
                        print("No existe un vehículo con esa placa.")
                    else:
                        del inventario[placa]
                        print("Vehículo inhabilitado exitosamente.")
                elif opcion_invitado == "3":
                    if inventario:
                        print("Vehículos disponibles:")
                        for placa, detalles in inventario.items():
                            print("Placa:", placa)
                            print("Marca:", detalles["Marca"])
                            print("Año:", detalles["Año"])
                            print("Modelo:", detalles["Modelo"])
                            print("------------------------")
                    else:
                        print("No hay vehículos disponibles.")
                elif opcion_invitado == "4":
                    print("Saliendo al menú de ingreso.")
                    break
                else:
                    print("Error, por favor vuelve a intentar.")

        elif opcion_ingreso == "4":
            sede_actual = None
            break

        elif opcion_ingreso == "5":
            print("El programa ha finalizado.")
            exit()

        else:
            print("Opción no válida. Por favor, elija una opción")
