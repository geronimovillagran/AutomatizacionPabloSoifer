# Dada una concesionaria de autos, 5 clientes van a pedir un auto, debe preguntarsele:
#
# *Nombre y apellido del comprador.
# *Marca
# *Puertas
# *Color
#
# Marcas posibles y sus precios:
#
# -Ford $100000
# -Chevrolet: $120000
# -Fiat: $80000
#
# -Por la cantidad de puertas se añade un precio:
#
# -2: $50000
# -4: $65000
# -5: $78000
#
# Dependiendo del color, se deben sumar:
#
# -Blanco: $10000
# -Azul: $20000
# -Negro: $30000
#
# Deben imprimirse los datos de cada compra y el precio total.

# obtener datos de comprador


def marcas(precio):
    salida = False

    while not salida:
        try:
            marca = int(
                input(
                    'Seleccione una de las marcas disponibles: 1-Ford $100000 , 2-Chevrolet: $120000 , 3-Fiat: $80000 '))
        except ValueError:
            print('No es una opcion valida')
        else:
            if marca == 1:
                auto = 'Ford'
                precio = precio + 100000
                break
            elif marca == 2:
                auto = 'Chevrolet'
                precio = precio + 120000
                break
            elif marca == 3:
                auto = 'Fiat'
                precio = precio + 80000
                break
            else:
                print('No es una opcion valida')

    return auto, precio


def puertas(precio):
    salida = False

    while not salida:
        try:
            puerta = int(input('Eliga la cantidad de puestas que desea: 1: 2-Puerta , 2: 4-Puertas , 3: 5-Puertas '))
        except ValueError:
            print('No es una opcion valida')
        else:
            if puerta == 1:
                cant_pue = '2 Puertas'
                precio = precio + 50000
                break
            elif puerta == 2:
                cant_pue = '4 Puertas'
                precio = precio + 65000
                break
            elif puerta == 3:
                cant_pue = '5 Puertas'
                precio = precio + 70000
                break
            else:
                print('No es una opcion valida')

    return cant_pue, precio


def colores(precio):
    salida = False

    while not salida:
        try:
            color = int(input('Selecione uno de los colores disponibles 1: Blanco , 2: Azul, 3: Negro'))
        except ValueError:
            print('No es una opcion valida')
        else:
            if color == 1:
                aut_col = 'Blanco'
                precio = precio + 10000
                break
            elif color == 2:
                aut_col = 'Azul'
                precio = precio + 20000
                break
            elif color == 3:
                aut_col = 'Negro'
                precio = precio + 3000
                break
            else:
                print('No es una opcion valida')

    return aut_col, precio


def llamado():
    listacliente = []
    largo = len(listacliente)
    salida = True

    while salida:
        salgo = int(input("1-Ingresar nuevo cliente:\n2- Salir\nOpcion: "))
        if salgo == 1:
            precio = 0
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido")
            marca, precio = marcas(precio)
            puerta, precio = puertas(precio)
            color, precio = colores(precio)

            if 4 < largo < 10:
                precio = precio * 0.90  # se obtiene el precio con el 10% de descuento

            elif 10 <= largo <= 51:
                precio = precio * 0.85  # se obtiene el precio con el 15% de descuento

            elif largo > 51:
                precio = precio * 0.82  # se obtiene el precio con el 18% de descuento

            diccionario_cliente = {
                'nombre': nombre, 'apellido': apellido, 'auto': marca, 'puertas': puerta, 'color': color,
                'total': precio
            }
            listacliente.append(diccionario_cliente)

        elif salgo == 2:
            salida = False
            break
        else:
            print('selecione una opcion valida')
    return listacliente


ventas = llamado()
for lista in ventas:
    print('El cliente {} {} compro un auto marca {} de color {} y {} a un precio total de {}'.format(lista['nombre'],
                                                                                                     lista['apellido'],
                                                                                                     lista['auto'],
                                                                                                     lista['color'],
                                                                                                     lista['puertas'],
                                                                                                     lista['total']))

''', lista['nombre'], lista['apellido'], 'compro un auto marca ', lista['auto'], ' de color ',
          lista['color'], 'y', lista['puertas'], ' a un precio total de ', lista['total'])'''
