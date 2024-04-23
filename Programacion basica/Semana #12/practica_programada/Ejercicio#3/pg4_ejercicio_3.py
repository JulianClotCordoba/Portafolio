# Julian Clot
# Universidad Fidelitas
# Programacion Basica

for i in range(1, 26):
    salario = int(input(f"Digite el salario del futbolista #{i}: "))
    b50000 = salario//50000
    salario %= 50000
    b20000 = salario//20000
    salario %= 20000
    b5000 = salario//5000
    salario %= 5000
    m500 = salario//500
    salario %= 500
    m100 = salario//100
    salario %= 100
    m25 = salario//25
    salario %= 25

    print(f"{b50000} billete de 50000")
    print(f"{b20000} billete de 20000")
    print(f"{b5000} billete de 5000")
    print(f"{m500} moneda de 500")
    print(f"{m100} moneda de 100")
    print(f"{m25} moneda de 25")

