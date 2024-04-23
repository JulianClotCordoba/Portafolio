#Julian Clot
#Universidad Fidelitas

# Practica #1
print("Hola, esta es una calculadora de figuras (triangulos y cuadrados), porfavor indique que figura quiere averiguar y sus respectivas medidas. ")

opcion = input("Indique 'C' si es cuadrado o 'T' si es triangulo: ")

if opcion == "C":
    lado_cuadrado = int(input("Indique el lado del cuadrado: "))
    perimetro = lado_cuadrado * 4
    print("El perimetro del cuadrado es: ", perimetro)
    area = lado_cuadrado * lado_cuadrado
    print("El area del cuadrado es: ", area)
elif opcion == "T":
    lado_triangulo = int(input("Indique el lado del triangulo: "))
    altura_triangulo = int(input("Indique la altura del triangulo: "))
    perimetro = lado_triangulo * 3
    print("El perimetro del triangulo es: ", perimetro)
    area = (lado_triangulo * altura_triangulo) / 2
    print("El area del triangulo es: ", area)
