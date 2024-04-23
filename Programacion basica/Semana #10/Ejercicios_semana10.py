#Julian Clot
# Universidad Fidelitas

# Ejercicio 1
matriz = [[86, 52, 90, 67],
          [41, 57, 64, 100],
          [80, 12, 100, 74],
          [100, 39, 51, 70]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] *= 2

for fila in matriz:
    print(fila)

# Ejercicio 2
matriz_estudiantes = [[86, 52, 90, 67],
                     [41, 57, 64, 100],
                     [80, 12, 100, 74],
                     [100, 39, 51, 70],
                     [99, 98, 96, 100]]

for x in matriz_estudiantes:
    suma = 0
    for numero in x:
        suma += numero
        porcentaje = suma / 4
    print(f"El porcentaje del estudiante {x} es: {porcentaje}")


# Ejercicio 2

l = 0
m = 0

espacios = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 5, 0],
            [0, 0, 0, 0]]

print("A continuacion son los campos que estan libres: ")
for fila in range(len(espacios)):
    for columna in range(len(espacios[fila])):
        if espacios[fila][columna] == 0:
            print(f"({fila},{columna})")

x = int(input("Dime la coordenada (x) para ubicar su espacio: "))
y = int(input("Dime la coordenada (y) para ubicar su espacio: "))

espacios[x][y] = 1
print("Obutvo su espacio", espacios)


