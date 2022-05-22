def main_ciudad():
    print("main ciudad")
    print("Curarse - 1")
    print("Salir - 2")
    choice = int(input("Opcion:.. "))
    if choice == 1:
        print("curado")
        player.vida = 40
        main_ciudad()
    if choice == 2:
        viajar()


def ciudad():
    print("ciudad")


def shop():
    print("shop")
    shop1 = ['Armas', 'Espada Corta', 3, 0]
    shop2 = ['Armas', 'Daga', 1, 0]
    shop3 = ['Armas', 'Espada Larga', 7, 0]
    shoplist = [shop1, shop2, shop3]
    for item in shoplist:
        itemtype = item[0]
        if itemtype == 'Armas':
            weapontype = itemtype[2]
            if weapontype == 0:
                tipo = 'One handed Sword'
                print(f"{item[1]} - Daño {item[2]} - tipo: {tipo}")
            if weapontype == 1:
                tipo = 'Two handed Sword'
                print(f"{item[1]} - Daño {item[2]} - tipo: {tipo}")
        if itemtype == 'Escudos':
            print(f"{item[1]} - Defensa {item[2]} - tipo: Fisico")
        if itemtype == 'Armaduras':
            armortype = item[2]
            if armortype == 0:
                tipo = 'Cabeza'
                print(f"{item[1]} - Defensa {item[2]} - tipo: {tipo}")
            if armortype == 1:
                tipo = 'Pecho'
                print(f"{item[1]} - Defensa {item[2]} - tipo: {tipo}")
            if armortype == 2:
                tipo = 'Brazos'
                print(f"{item[1]} - Defensa {item[2]} - tipo: {tipo}")
            if armortype == 3:
                tipo = 'piernas'
                print(f"{item[1]} - Defensa {item[2]} - tipo: {tipo}")
main_ciudad()
