
# Ejercicio 1:
suma_vueltas = 0
suma_pits = 0

for i in range(1, 11):
    tiempo = float(input(f"Ingrese el tiempo de vuelta {i} en segundos: "))
    suma_vueltas += tiempo

for i in range(1, 11):
    tiempo = float(input(f"Ingrese el tiempo de PITS {i} en segundos: "))
    suma_pits += tiempo

promedio_vueltas = suma_vueltas / 10
promedio_pits = suma_pits / 10

total = suma_vueltas + suma_pits
porcentaje = (suma_pits / total) * 100

print("Tiempo promedio por vuelta: ", promedio_vueltas)
print("Tiempo promedio por los pits: ", promedio_pits)
print("Porcentaje del tiempo de pits con respecto al tiempo de vuelta: ", porcentaje)


# Ejercicio 2:
cantidad_estudiantes = int(input("A cuantos niños se les analizará la estadistica: "))

menos_100cm = 0
entre_100cm_120cm = 0
entre_121cm_130cm = 0
entre_131cm_140cm = 0
mas_140cm = 0

suma_estaturas = 0

for i in range(1, cantidad_estudiantes):
    estaturas = int(input(f"Cual es la estatura del estudiante #{i}"))

    if estaturas < 100:
        menos_100cm += 1
    elif estaturas < 120 > 100:
        entre_100cm_120cm += 1
    elif estaturas < 130 > 121:
        entre_121cm_130cm += 1
    elif estaturas > 140 < 131:
        entre_131cm_140cm += 1
    elif estaturas > 140:
        mas_140cm += 1

    suma_estaturas += estaturas

    promedio = suma_estaturas / cantidad_estudiantes


print("Promedio de todas las estaturas: ", promedio)
print("Cantidad de estudiantes con estatura menor a 100cm: ", menos_100cm)
print("Cantidad de estudiantes con estatura entre 100cm y 120cm: ", entre_100cm_120cm)
print("Cantidad de estudiantes con estatura entre 121cm y 130cm: ", entre_121cm_130cm)
print("Cantidad de estudiantes con estatura entre 131cm y 140cm: ", entre_131cm_140cm)
print("Cantidad de estudiantes con estatura mayor a 140cm: ", mas_140cm)


# Ejercicio 3:
valor = int(input("Digite un numero: "))

contador = 0
numero = valor
while contador < 10:
    if numero % valor == 0:
        print(numero)
        contador += 1
    numero += 1

# Ejercicio 4:
for i in range(1, 15):
    salario = int(input(f"Digite el salario de la persona #{i}: "))
    if salario < 500:
        diferencia = 500 - salario
        print(f"A la persona #{i} le faltan {diferencia} para llegar al salario mínimo.")
    else:
        print(f"La persona #{i} tiene un salario de {salario} pesos.")

                

