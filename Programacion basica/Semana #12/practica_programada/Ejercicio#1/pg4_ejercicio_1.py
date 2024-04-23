# Universidad fidelitas
# Programacion basica
# Practica de integracion de conocimientos

# Ejercicio 1
cursos = {"curso1": 5, "curso2": 5, "curso3": 5}
notas_curso1 = []
notas_curso2 = []
notas_curso3 = []
estudiantes_aprovados = 0
estudiantes_reprovados = 0

for i in range(1, 6):
    print("Digite las notas de los estudiantes del primer curso: ")
    nota = int(input(f"Digite la nota del {i} estudiante: "))
    notas_curso1.append(nota)

for x in range(1, 6):
    print("Digite las notas de los estudiantes del segundo curso: ")
    nota = int(input(f"Digite la nota del {x} estudiante: "))
    notas_curso2.append(nota)

for y in range(1, 6):
    print("Digite las notas de los estudiantes del tercer curso: ")
    nota = int(input(f"Digite la nota del {y} estudiante: "))
    notas_curso3.append(nota)

notas = [notas_curso1, notas_curso2, notas_curso3]

print("Notas de los estudiantes en cada curso:")
for i, notas_curso in enumerate(notas, start=1):
    print(f"Curso {i}: {notas_curso}")

print("Promedio de notas de los estudiantes: ")
promedio = (sum(notas_curso1) + sum(notas_curso2) + sum(notas_curso3)) / 15
print(promedio)

print("Promedio de notas de cada uno de los grupos: ")
promedio_1 = (sum(notas_curso1)) / 5
promedio_2 = (sum(notas_curso2)) / 5
promedio_3 = (sum(notas_curso3)) / 5

print("El promedio de notas en el primer curso es de: ", promedio_1)
print("El promedio de notas del segundo curso es de: ", promedio_2)
print("El promedio de notas del tercer curso es de: ", promedio_3)

for x in [notas_curso1, notas_curso2, notas_curso3]:
    for y in x:
        if y > 70:
            estudiantes_aprovados+=1
        elif y < 70:
            estudiantes_reprovados+=1

print("Aprovados: ", estudiantes_aprovados)
print("Reprovados: ", estudiantes_reprovados)

ma = notas_curso1[0]
me = notas_curso1[0]

for x in [notas_curso1, notas_curso2, notas_curso3]:
    for y in x:
        if y > ma:
            ma = y
        elif y < me:
            me = y

print("La mayor nota: ", ma)
print("La menor nota: ", me)
        