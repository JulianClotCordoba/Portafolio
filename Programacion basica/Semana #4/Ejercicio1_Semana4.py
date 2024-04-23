# Julian Clot
# Universidad Fidelitas

# Ejercicio 1
salario = input("Ingrese su salario: ")
salario = float(salario)

if salario < 1000:
    salario = salario + salario + 0.15
    print("Su salario es: ", salario)

# Ejercicio 2
salario = int(input("Cual es el salario: "))
categoria = int(input("Cual es tu categoria: "))

if categoria == 1:
    porcentaje = salario * 0.10
    print("El salario es: ", porcentaje)
if categoria == 2:
    porcentaje = salario * 0.12
    print("El salario es: ", porcentaje)
if categoria == 3:
    porcentaje = salario * 0.15
    print("El salario es: ", porcentaje)
if categoria == 4:
    porcentaje = salario * 0.20

# Ejercicio 3
estudiante = input("Nombre del estudiante: ")
materia = input("Nombre del curso: ")
nota = int(input("Digite la nota: "))

if nota >= 70:
    print("El estudiante", estudiante, " en la asignacion de ", materia, " quedo aprovado con una nota de ", nota)
else:
    print("El estudiante ", estudiante, "quedo reprobado de la materia ", materia, "con una nota de ", nota)

# Ejercicio 4
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
numero4 = float(input("Ingrese el cuarto número: "))

mayor = numero1

if numero2 > mayor:
    mayor = numero2
if numero3 > mayor:
    mayor = numero3
if numero4 > mayor:
    mayor = numero4

print("El número mayor es:", mayor)

# Ejercicio 5
numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))

if numero1  >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3

if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    menor = numero2
else:
    menor = numero3

medio = ((numero1 + numero2 + numero3) - mayor) - menor

print("Los numero ordenados son: ", mayor, medio, menor)

# Ejercicio 6

anho = int(input("Ingrese el año de nacimiento: "))

if (anho % 4 == 0 and anho % 100 != 0) or (anho % 400 == 0)
    print("El año es bisiesto. ")
else:
    print("El año no es bisiesto")
