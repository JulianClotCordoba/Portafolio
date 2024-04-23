#Julian Clot
#Universidad Fidelitas

# Ejercicio 1
for i in range(20, 41, 2):
    print(i, i**2)

# Ejercicio 2
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
nota_aprobacion = 70
contador_aprobados = 0
contador_reprobados = 0

nota_mayor = 0  
nota_menor = 100  

while cantidad_estudiantes > 0:
    estudiante = input("Nombre del estudiante: ")
    nota = int(input("Nota del estudiante: "))
    
    if nota > nota_mayor:
        nota_mayor = nota
    if nota < nota_menor:
        nota_menor = nota
    
    if nota >= nota_aprobacion:
        contador_aprobados += 1
    else:
        contador_reprobados += 1
    
    cantidad_estudiantes -= 1

print("Nota mayor:", nota_mayor)
print("Nota menor:", nota_menor)
print("Cantidad de aprobados:", contador_aprobados)
print("Cantidad de reprobados:", contador_reprobados)

# Ejercicio 3
colaboradores = 10

for i in range(colaboradores):
    salario = int(input("Indique el salario de cada trabajador: "))
    deduccion = salario * (9 / 100)
    salario_total = salario - deduccion

    print(f"El salario total del trabajador {i+1}: ", salario_total)

# Ejercicio 4
valores = 10
suma = 0

while  valores > 0:
    numeros = int(input("Digite 10 numero enteros: "))

    if numeros % 2 == 0:
        suma += numeros
    valores -= 1

print("La suma de los numeros pares es: ", suma)

# Ejercicio 5
numero_decimal = int(input("Indique un numero decimal, positivo, entero: "))
binario = ''

if numero_decimal == 0:
    binario = "0"
else: 
    while numero_decimal > 0:
        binario = str(numero_decimal % 2) + binario
        numero_decimal = numero_decimal // 2

print(binario)
               

    

               
