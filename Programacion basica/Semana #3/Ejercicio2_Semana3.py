# Julian Clot
# Universidad Fidelitas
# Practica 2


#Ejercicio 1
nombre_producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad comprada: "))
precio_unitario = float(input("Ingrese el precio unitario del producto: "))

total_sin_iva = cantidad * precio_unitario

iva = total_sin_iva * 0.13

total_con_iva = total_sin_iva + iva

print("Detalle de la compra:")
print("Producto:", nombre_producto)
print("Cantidad:", cantidad)
print("Precio unitario: ", precio_unitario)
print("Total sin IVA: ", total_sin_iva)
print("IVA (13%): ", iva)
print("Total con IVA: ", total_con_iva)

# Ejercicio 2
hora_entrada = int(input("Hora de entrada (en horas): "))
minuto_entrada = int(input("Minuto de entrada (en minutos): "))
segundo_entrada = int(input("Segundo de entrada (en segundos): "))
hora_salida = int(input("Hora de salida (en horas): "))
minuto_salida = int(input("Minuto de salida (en minutos): "))
segundo_salida = int(input("Segundo de salida (en segundos): "))

tiempo_entrada_segundos = hora_entrada * 3600 + minuto_entrada * 60 + segundo_entrada
tiempo_salida_segundos = hora_salida * 3600 + minuto_salida * 60 + segundo_salida
tiempo_laborado_segundos = tiempo_salida_segundos - tiempo_entrada_segundos

print("\nTiempo laborado:", tiempo_laborado_segundos, "segundos")

#Ejercicio 3
nombre = input("Nombre del funcionario: ")
cedula = input("Número de cédula: ")
salario_bruto = float(input("Salario bruto: "))

ccss = salario_bruto * 0.08
banco_popular = salario_bruto * 0.01
total_deducciones = ccss + banco_popular
salario_neto = salario_bruto - total_deducciones

print("Información del funcionario:")
print("Empleado:", nombre)
print("Identificación:", cedula)
print("Salario bruto: ", salario_bruto)
print("CCSS (8%): ", ccss)
print("Banco Popular (1%): ", banco_popular)
print("Total deducciones: ", total_deducciones)
print("Salario neto: ", salario_neto)

# Ejercicio 4
nombre_producto = input("Ingrese el nombre del producto: ")
precio_san_jose = float(input("Precio en San José: "))
precio_heredia = float(input("Precio en Heredia: "))
precio_alajuela = float(input("Precio en Alajuela: "))

precio_promedio = (precio_san_jose + precio_heredia + precio_alajuela) / 3

print("Información del producto:", nombre_producto)
print("Precio en San José: ", precio_san_jose)
print("Precio en Heredia: ", precio_heredia)
print("Precio en Alajuela: ", precio_alajuela)
print("Precio promedio: ", precio_promedio)

#Ejercicio 5
nombre_vendedor = input("Nombre del vendedor: ")
total_unidades_vendidas = int(input("Total de unidades vendidas: "))
precio_articulo = float(input("Precio del artículo vendido: "))

if precio_articulo <= 20000:
    comision = precio_articulo * 0.03
elif precio_articulo < 50000:
    comision = precio_articulo * 0.05
else:
    comision = precio_articulo * 0.10

print("Información de la comisión:")
print("Nombre del vendedor:", nombre_vendedor)
print("Total de unidades vendidas:", total_unidades_vendidas)
print("Precio del artículo:", precio_articulo)
print("Comisión: ", comision)

