
vendedor1 = input("Cual es el nombre del vendedor numero 1: ")
monto1 = input("Monto del vendedor 1: ")
vendedor2 = input("Cual es el nombre del vendedor numero 2: ")
monto2 = input("Monto del vendedor 2: ")
vendedor3 = input("Cual es el nombre del vendedor numero 3: ")
monto3 = input("Monto del vendedor 3: ")

archivo = open("monto_de_vendedor.txt", "w")


def escribir_archivo():
    archivo.write("\n" + vendedor1 + "\n" + monto1)
    archivo.write("\n" + vendedor2 + "\n" + monto2)
    archivo.write("\n" + vendedor3 + "\n" + monto3)
    archivo.close()
    abrir_archivo()

def abrir_archivo():
    archivo_2 = open("monto_de_vendedor.txt", "r")
    contenido_del_archivo = archivo_2.read()
    print(contenido_del_archivo)
    archivo_2.close()

escribir_archivo()