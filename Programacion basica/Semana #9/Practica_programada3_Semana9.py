productos = {
    "Enlatados": [],
    "Limpieza": [],
    "Carnes": [],
    "Granos": []
}

while True:
    print("1. Agregar productos")
    print("2. Eliminar uno de los productos")
    print("3. Actualizar uno de los productos")
    print("4. Ver productos")

    opcion = int(input("¿Que opción deseas elegir? "))

    if opcion == 1:
        print("1. Articulos enlatados")
        print("2. Productos de limpieza")
        print("3. Carnes")
        print("4. Granos(Arroz, frijoles, entre otros)")
        opcion_uno = int(input("¿Que tipo de articulo deseas ingresar? (1-4) "))

        if opcion_uno == 1:
            articulo_enlatado = input("¿Que articulo deseas incorporar? ")
            if articulo_enlatado in productos["Enlatados"]:
                print("Ya existe")
            else:
                productos["Enlatados"].append(articulo_enlatado)

        elif opcion_uno == 2:
            producto_limpieza = input("¿Que producto de limpieza deseas incorporar? ")
            if producto_limpieza in productos["Limpieza"]:
                print("Ya existe")
            else:
                productos["Limpieza"].append(producto_limpieza)

        elif opcion_uno == 3:
            carne = input("¿Que carne deseas incorporar? ")
            if care in productos["Carne"]:
                print("Ya existe")
            else:
                productos["Carnes"].append(carne)

        elif opcion_uno == 4:
            grano = input("¿Que grano deseas incorporar? ")
            if grano in productos["Granos"]:
                print("Ya existe")
            else:
                productos["Granos"].append(grano)

    elif opcion == 2:
        print("Enlatados")
        print("Limpieza")
        print("Carnes")
        print("Granos")
        eliminar_articulo = input("¿Cual es el tipo o grupo de articulos al que quieres eliminar el producto? ")
        eliminar_producto = input("¿Cual es el producto que quieres eliminar? ")
        productos[eliminar_articulo].remove(eliminar_producto)

    elif opcion == 3:
        print("Enlatados")
        print("Limpieza")
        print("Carnes")
        print("Granos")
        actualizar_articulo = input("¿Cual es el tipo o grupo de articulos al que quieres eliminar el producto? ")
        actualizar_producto = int(input("¿Cual es el indice (1...) del producto que quieres eliminar? (Toma en cuenta que el primero es el '0')"))
        nuevo_producto = input("¿Que nuevo producto quieres incorporar? ")

        productos[actualizar_articulo][actualizar_producto] = nuevo_producto

    elif opcion == 4:
        print(productos)
