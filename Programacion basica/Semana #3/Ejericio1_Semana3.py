# Julian Clot
# Universidad Fidelitas
# Practica 1

#Ejercicio 1
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")

print("Bienvenido, estimado", nombre, apellido, apellido2)

#Ejercicio 2
numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))

operacion = int(input("Ingrese la operacion que quiera realizar: 1. Suma, 2. Resta, 3. Multiplicacion, 4. Division "))

if operacion == 1:
    print("El resultado de la suma es ", numero1 + numero2)
elif operacion == 2:
    print("El resultado de la resta es ", numero1 - numero2)

elif operacion == 3:
    print("El resultado de la multiplicacion es ", numero1 * numero2)

elif operacion == 4 and numero2 != 0:
    print("El resultado de la division es ", numero1 / numero2)
else:
    print(" Error")

# Ejercicio 3

lado = int(input("Indica el lado del cuadrado: ")

area = lado * lado
perimetro = lado * 4

print("El area del cuadrado es: ", area, "El perimetro del cuadrado es: ", perimetro)

# Ejercicio 4

Luis = 34
Pedro = 52


print("Edades iniciales")
print("La edad de luis es: ", luis)
print("La edad de pedro es: ", pedro)

print("Edades intercambiadas")
print("La edad de luis es: ", pedro)
print("La edad de pedro es: ", luis)

# Ejercicio 5

numero = int(input("Indique el numero: ")
exponente = int(input("Indique el exponente: ")

potencia = numero ** exponente

print("El resultado de la potencia es: ", potencia)
