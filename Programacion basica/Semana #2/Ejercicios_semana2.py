#Julian CLot

#Ejercico 1
print("Ejercicio 1")
a = input("Ingrese el valor a: ")
b = input("Ingrese el valor b: ")
c = input("Ingrese el valor c: ")
d = input("Ingrese el valor d: ")

print(d, c, b, a)

# Ejercicio 2
print("Ejercicio 2")

edad = int(input("Ingrese la edad: "))
suma = edad + 5
print("Dentro de 5 años, tendra: ", suma)

# Ejercicio 3
print("Ejercicio 3")
a = int(input("Digite un numero entero: "))
b = int(input("Digite un numero entero: "))

expresion = ((a + b) * 2)/3
print(expresion)

#Ejercicio 4
print("Ejercicio 4")
a = int(input("Digite un numero: "))

cuadrado = a ** 2
cubo = a ** 3
print("Cuadrado: ", cuadrado, "Cubo: ", cubo)

#Ejercicio 5
print("Ejercicio 5")
altura = int(input("Digite la altura: "))
base = int(input("Digite la base: "))

area = base * altura
perimetro = base * 4

print("Area: ", area, "Perimetro: ", perimetro)

#Ejercicio 6
print("Ejericio 6")
distancia = int(input("Cual es su distancia en kilometros de su casa a la universidad: "))
costo_por_kilometro = 15
dias = 2

costo_universidad = costo_por_kilometro * distancia
total = costo_universidad * 15
print("El costo total para ir a la universidad es: ", total)

#Ejercicio 7
print("Ejercicio 7")
usuario1 = int(input("Digite la edad de la primera persona: "))
usuario2 = int(input("Digite la edad de la segunda persona: "))
usuario3 = int(input("Digite la edad de la tercera persona: "))
usuario4 = int(input("Digite la edad de la cuarta persona: "))
usuario5 = int(input("Digite la edad de la quinta persona: "))

promedio = (usuario1 + usuario2 + usuario3 + usuario4 + usuario5) / 5
print("El promedio es: ", promedio)


#Ejercicio 8
print("Ejercicio 8")
horas = int(input("Cantidad de horas laboradas: "))
salario_base = 150 * 705.6
deduccion_social = 10.5
asociacion_solidarista = 5

salario_mensual = salario_base - (deduccion_social / 100) - (asociacion_solidarista / 100)

print("El salario mensual es de: ", salario_mensual)

#Ejercicio 9
print("Ejercicio 9")
ingresos = int(input("Cuales son sus ingresos: "))
gastos_mensuales = int(input("Cuales son sus gastos mensuales: "))


porcentaje_de_gasto = (ingresos - gastos_mensuales) / 100
print("El rubro de sus gastos mensuales en base sus ingresos son: ", porcentaje_de_gasto)
