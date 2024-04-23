#Julian Clot
#Universidad Fidelitas

# Ejercicio 1
dias = {}
total_kilometros = 0


for x in range(1, 8):
    kilometros = int(input(f"Cuantos kilometros recorriste el dia {x}: "))
    dias[f"Dia {x}"] = kilometros
    total_kilometros += kilometros
print("Estos son los kilometros por dia en la semana: ", dias)
print("El total de kilometros en la semana son: ", total_kilometros)

# Ejercicio 2
personas = {}

for i in range(1, 11):
    nombres = input(f"Ingrese el nombre {i}: ")
    personas[nombres] = i
print("A las siguientes personas se les asignaron el numero de butaca: ", personas)

# Ejercicio 3
palabra = input("Ingrese una palabra: ")
palabra_al_reves = ""

for i in range(len(palabra) - 1, -1, -1):
    palabra_al_reves += palabra[i]

print("La palabra al reves es:", palabra_al_reves)

# Ejercicio 4

ganancias = {}

for k in range(1, 8):
    monto = int(input(f"Digite el monto del día {k}: "))
    ganancias[k] = monto

ganancia_minima = ganancias[1]
ganancia_maxima = ganancias[1]

for dia, ganancia in ganancias.items():
    if ganancia < ganancia_minima:
        ganancia_minima = ganancia
    if ganancia > ganancia_maxima:
        ganancia_maxima = ganancia

print("El dia que ganaste mas fue la suma de: ", ganancia_maxima)
print("El dia que ganaste menos fue la suma de: ", ganancia_minima)
