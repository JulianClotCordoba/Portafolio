# Julian Clot
# Universidad Fidelitas

cuenta_meses = [0] * 12
edades = []
cantidad_estudiantes = int(input("Digite la cantidad de estudiantes: "))
contador = 0

while contador < cantidad_estudiantes:

  mes = int(input("Ingrese el mes de cumpleaños (1-12): "))
  edad = int(input("Ingrese la edad: "))
  edades.append(edad)
  cuenta_meses[mes-1] += 1
  contador += 1
  
for i in range(0, 12):
  print(f"Estudiantes en el mes {i+1}: {cuenta_meses[i]}")
  
promedio = sum(edades) / len(edades)
print(f"Promedio de edades: {int(promedio)}")
