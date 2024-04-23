letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def binario(numero):
    binario = ""
    while numero > 0:
        numero = numero // 2
        residuo = numero % 2
        binario = str(residuo) + binario
    return binario

def octal(numero):
    octal = ""
    while numero > 0:
        numero = numero // 8
        residuo = numero % 8
        octal = str(residuo) + octal
    return octal

def hexadecimal(numero):
    hexadecimal = ""
    while numero > 0:
        residuo = numero % 16
        if residuo < 10:
            hexadecimal = str(residuo) + hexadecimal
        else:
            hexadecimal = letras[residuo - 10] + hexadecimal
        numero = numero // 16
    return hexadecimal or "0"

numero = int(input("Digite un numero para transoformar: "))
print("Binario: ", binario(numero))
print("Octal: ", octal(numero))
print("Hexadecimal: ", hexadecimal(numero))
