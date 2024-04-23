lunes = {}
martes = {}
miercoles = {}
jueves = {}
viernes = {}

while True:
    print("Seleccione el día que desea ingresar o mostrar resultados y salir:")
    print("[1] Lunes")
    print("[2] Martes")
    print("[3] Miércoles")
    print("[4] Jueves")
    print("[5] Viernes")
    print("[6] Mostrar resultados y salir")

    opcion = int(input("Elija una opción: "))

    if opcion in range(1, 6):
        dia = ""
        if opcion == 1:
            dia = lunes
        elif opcion == 2:
            dia = martes
        elif opcion == 3:
            dia = miercoles
        elif opcion == 4:
            dia = jueves
        elif opcion == 5:
            dia = viernes

        nombre = input("Digite su nombre para identificar la temperatura: ")
        temperatura = int(input("Digite la temperatura: "))
        dia[nombre] = temperatura

    elif opcion == 6:
        for dia, datos in [("Lunes", lunes), ("Martes", martes), ("Miércoles", miercoles), ("Jueves", jueves), ("Viernes", viernes)]:
            if datos:
                promedio = sum(datos.values()) / len(datos)
                max_temp = max(datos.values())
                min_temp = min(datos.values())
                max_persona = max(datos, key=datos.get)
                min_persona = min(datos, key=datos.get)
                print(f"{dia}:")
                print(f"- Temperatura promedio: {promedio}")
                print(f"- Temperatura máxima: {max_temp} | {max_persona}")
                print(f"- Temperatura mínima: {min_temp} | {min_persona}")
            else:
                print(f"{dia}: No hay datos.")
        print("Hasta luego.")
        break

    else:
        print("Opción inválida. Inténtelo de nuevo.")
