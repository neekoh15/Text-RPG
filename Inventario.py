inventario = []


def droplist():
    print(f" NOMBRE_BICHO muere - su botin cae al piso...")
    drop1 = ['Consumible', 'Pocion de vida', 1, 5]
    drop2 = ['Consumible', 'Oro', 57, 0]
    drop3 = ['Armas', 'Espada Larga', 7, 1]
    drop4 = ['Armas', 'Espada Corta', 3, 0]
    drop5 = ['Escudos', 'Escudo de madera', 2, 0]
    temp = [drop1, drop2, drop3, drop4, drop5]
    for x in temp:
        if x[0] == 'Consumible':
            print(x[1], "- cantidad: ", x[2])
        if x[0] == 'Armas':
            if x[3] == 0:
                tipo = 'One-handed sword'
                print(x[1], "- Daño: ", x[2], "tipo: ", tipo)
            if x[3] == 1:
                tipo = 'Two-handed sword'
                print(x[1], "- Daño: ", x[2], "tipo: ", tipo)
        if x[0] == 'Escudos':
            if x[3] == 0:
                tipo = 'Fisico'
                print(x[1], "- Defensa: ", x[2], "tipo: ", tipo)
            if x[3] == 1:
                tipo = 'Magico'
                print(x[1], "- Defensa: ", x[2], "tipo: ", tipo)
    print("Recoger Drop?")
    print("1 - SI")
    print("2 - NO")
    choice = int(input("Recoger drop?.. "))
    if choice == 1:
        Drops = [drop1, drop2, drop3, drop4, drop5]
        # print(Drops)
        for i in inventario:
            for j in Drops:
                if i.nombre == j[1]:
                    # print("doble")
                    i.cantidad = i.cantidad + j[2]
                    Drops.remove(j)
        for x in Drops:
            i = x[0]
            if i == 'Consumible':
                aux1 = x[1]
                aux2 = x[2]
                aux3 = x[3]
                x = Objeto_consumible(aux1, aux2, aux3)
            if i == 'Armas':
                aux1 = x[1]
                aux2 = x[2]
                aux3 = x[3]
                x = Armas(aux1, aux2, aux3)
            if i == 'Escudos':
                aux1 = x[1]
                aux2 = x[2]
                aux3 = x[3]
                x = Escudos(aux1, aux2, aux3)
            inventario.append(x)
        # print(Drops)


def verinventario():
    print("Abriendo inventario: ")
    for x in inventario:
        if isinstance(x, Objeto_consumible) == True:
            print(f"{x.nombre} - Cantidad: {x.cantidad}")
        if isinstance(x, Armas) == True:
            if x.atributo == 0:
                tipo = 'One-handed sword'
                print(f"{x.nombre} - Daño: {x.daño} - Tipo:{tipo}")
            if x.atributo == 1:
                tipo = 'Two-handed sword'
                print(f"{x.nombre} - Daño: {x.daño} - Tipo:{tipo}")
        if isinstance(x, Escudos) == True:
            if x.atributo == 0:
                tipo = 'Fisico'
                print(f"{x.nombre} - Defensa: {x.defensa} - Tipo:{tipo}")
            if x.atributo == 1:
                tipo = 'Magico'
                print(f"{x.nombre} - Defensa: {x.defensa} - Tipo:{tipo}")
