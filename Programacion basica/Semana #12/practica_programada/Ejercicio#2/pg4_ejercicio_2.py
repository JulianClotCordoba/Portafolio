#Julian Clot
#Universidad Fidelitas
#Programacion basica

dias = {}

# Primer proceso
for i in range(1, 6):
    dias[f"dia{i}"] = {}
    for j in range(1, 5):
        servicios = int(input(f"Digite la cantidad de pasajeros en el servicio #{j} del día {i}: "))
        if servicios <= 60:
            dias[f"dia{i}"][f"servicio{j}"] = servicios
        else:
            print("Sobrepaso la cantidad máxima de pasajeros.")
            break

promedio_general = 0
total_dias_con_servicios = 0


# Segundo proceso
for dia, servicios in dias.items():
    if servicios:
        total_dias_con_servicios += 1
        promedio_servicios = sum(servicios.values()) / len(servicios)
        promedio_general += promedio_servicios

if total_dias_con_servicios > 0:
    promedio_general /= total_dias_con_servicios
    print("El promedio general de todos los días es:", promedio_general)
else:
    print("No se registró ningún servicio.")


# Tercer proceso
for dia, servicios in dias.items():
    if servicios:
        maximo_pasajeros = 0
        mejor_servicio = None

        minimo_pasajeros = 10000
        peor_servicio = None

        for servicio, pasajeros in servicios.items():
            if pasajeros > maximo_pasajeros and pasajeros <= 60:
                maximo_pasajeros = pasajeros
                mejor_servicio = servicio

            if pasajeros < minimo_pasajeros and pasajeros <= 60:
                minimo_pasajeros = pasajeros
                peor_servicio = servicio

        if mejor_servicio is not None:
            print(f"El mejor servicio del {dia} es el {mejor_servicio} con un total de {maximo_pasajeros} pasajeros.")
        if peor_servicio is not None:
            print(f"El peor servicio del {dia} es el {peor_servicio} con un total de {minimo_pasajeros} pasajeros.")
    else:
        print(f"No se registraron servicios en el día {dia}.")

