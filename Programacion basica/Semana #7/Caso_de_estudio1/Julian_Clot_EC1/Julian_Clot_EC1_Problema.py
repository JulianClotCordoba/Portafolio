# Universidad Fidelitas
# Julian Clot Cordoba

import random

semana1 = random.randint(1, 100)
semana2 = random.randint(1, 100)
semana3 = random.randint(1, 100)
semana4 = random.randint(1, 100)
semanas = {"semana1": semana1, "semana2": semana2, "semana3": semana3, "semana4": semana4}

premio_aporte = {"1": {"Aporte": 500, "Premio": "Hamburguesa con papas y gaseosa"},"2": {"Aporte": 1000, "Premio": "Cupón cena para 2 personas"},"3": {"Aporte": 2000, "Premio": "Un día en el parque de diversiones con transporte y comida pago para 3 personas"},"4": {"Aporte": 5000, "Premio": "Fin de semana todo incluido en hotel paradisiaco para 2 personas"}}

usuario = {}
semana_elegida = random.randint(1, 4)

for semana in semanas:
    monto_total = 0

    print("______________________________")
    print("A continuacion, ingrese su nombre, cedula y el monto que usted aporto")
    print("______________________________")

    for i in range(1, 101):
        print("________")
        nombre = input("Digite su nombre: ")
        cedula = input("Digite su cédula: ")
        monto = int(input("Digite el monto que usted aportó: "))

        monto_total += monto

        if i == semana_elegida:
            usuario = {"nombre": nombre, "cedula": cedula, "monto": monto}
            premio = premio_aporte[str(i)]["Premio"]
            print("______________________")
            print("Felicidades ", nombre, " has ganado la rifa, tu premio es ", premio)
            print("______________________________")
            break

    print("______________________________")
    print("El monto total recaudado para la",semana, "es: ", monto_total)
    print("_____________________")

