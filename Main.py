import random
import pandas as pd
import numpy as np

class Player:
    def __init__(self, nombre, vida, ataque, defensa, atributo, posicion):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque  # daño fisico total
        self.defensa = defensa
        self.atributo = atributo  # = 0 , reservado para efectos elementales o demas, queseyo jaja
        self.posicion = posicion  # contador para moverse en el mapa
"""class Bichos: #reemplazado por -> Creatures
    def __init__(self, nombre, vida, daño, atributo):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
        self.atributo = atributo  # reservado para caracteristicas especiales (corrupto, enfermo, venenoso etc..)
"""
class Objeto_consumible:
    def __init__(self, nombre, cantidad, atributo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.atributo = atributo  # reservado para tipo de efecto ej: curaciones
class Armas:
    def __init__(self, nombre, daño, tipo, atributo):
        self.nombre = nombre
        self.daño = daño
        self.tipo = tipo  # 0 para armas de 1 mano, 1 para dos manos
        self.atributo = atributo  # reservado para daño de elementos (fuego hielo veneno etc..)
        # daño normal -> atributo = o
class Escudos:
    def __init__(self, nombre, defensa, atributo):
        self.nombre = nombre
        self.defensa = defensa
        self.atributo = atributo  # 0 para fisico, 1 para magico
class Armaduras:
    def __init__(self, nombre, defensa, lugar, atributo):
        self.nombre = nombre
        self.defensa = defensa
        self.lugar = lugar  # 0 cabeza , 1 pecho , 2 brazos, 3 piernas
        self.atributo = atributo  # 0 para fisico, 1 para magico
class Creatures:
    def __init__(self, nombre, vida, ataque, bioma, atributo):
        # print("criatura agregada a clase Creatures")
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = bioma
        self.atributo = atributo #


def main_ciudad():

    print(f"Bienvenido a Ciudad Capital!")
    print("Aqui encontraras muchas actividades para realizar!")
    def ciudad():
        # Proximas cosas a agregar: Taberna (Quests aca) - Barracas -(Aprender Clase) - Alquimista (Pociones) - Herrero (Armaduras y armas)
        print("Hechar un vistazo a la ciudad - 1") # Investigar permitiria encontrar items y quest especiales (?
        print("Vistar al curandero - 2")
        # if questtracker == 0:
          #  print("Irse - 3")
        # if questtracker == 1:
          #  print("Irse - 3")
        print("Irse - 3")
        choice = int(input("Opcion:.. "))
        global questtracker
        if choice == 1:
            print("Miras a tu alrededor y no percibes nada fuera de lo normal")
            if questtracker == 0:
                print("Excepto por un pequeño niño sentado en uno de los bancos, llorando..")
                print("Dejar de fizgonear y ocuparme de mis asuntos - 1")
                print("Acercarse al pequeño niño - 2")
                choice = int(input(f"Narrador: {player.nombre}, que quieres hacer?: .. "))
                if choice == 1:
                    ciudad()
                if choice == 2:
                    print("Te acercas al niño y te cuenta sus problemas, por algun motivo..")
                    print("- QUEST ACEPTADA - {Encuentrar la familia del niño lloron}")
                    questtracker = 1
                    ciudad()
            if questtracker == 1:
                print("Excepto por el pequeño mocoso, que sigue llorizqueando..")
                ciudad()


        if choice == 2:
            print("Curandero: Quien se atreve a interrumpir mis actividades!?")
            if player.vida == 40:
                print(f"Curandero: Oh! Pero si no tienes ni un razguño! ¿Que quieres de mi?")
                print("Curandero: Vete ya mismo, estoy ocupado")
                print(f"{player.nombre}: ... ")
                print("Vuelves a las calles de la ciudad")

            else:
                print("Han curado tus heridas")
                player.vida = 40
                print("Vuelves a las calles de la ciudad")
            ciudad()

        if choice == 3:
            viajar()
    ciudad()
def main_desierto():
    global firsttimedesert, clear
    if firsttimedesert == 1:
        print("Viajar a la Estepa Desertica")
    def desierto():
        print("Investigar - 1")
        print("Salir - 2")
        choice = int(input("Opcion:.. "))
        if choice == 1:
            print("investigando")
            desierto()
        if choice == 2:
            viajar()
    if firsttimedesert == 0:
        print("Continuas viajando a traves del bosque")
        print("A medida que avanzas por el bosque, el camino se torna dificultoso")
        print("La malesa se torna cada vez mas y mas densa, y de repente descubres que el camino frente a ti se encuentra bloqueado..")
        print(f"Narrador : Oye {player.nombre}, el camino parece bloqueado, que haremos ahora? ..")
        print("Retroceder, parece peligroso y no sabemos que nos espera detras del bloqueo - 1")
        print("Atravesar el bloqueo a la fuerza - 2")
        choice =int(input("Eliges: .. "))
        if choice == 1:
            print("Te das la vuelta y regresas al bosque")
            player.posicion = player.posicion -1
            main_bosque()
        if choice == 2:
            print("A la fuerza te haces paso por el sendero.. ")
            print("Breve descripcion del paisaje e introduccion a la Estepa Desertica")
            firsttimedesert = 1
            desierto()
    desierto()
def main_bosque():
    print("Te adentras en las profundidades del Bosque.. ")
    def bosque():
        global  bosquefirstfight
        print(f"Narrador: {player.nombre}, que deseas hacer? ..")
        print("Investigar el lugar - 1")
        print("Continuar viajando - 2")
        choice = int(input("Opcion:.. "))
        if choice == 1:
            if bosquefirstfight == 0:
                print("Narrador: Miras a tu alrededor, y a primera vista no parace haber nada fuera de lo normal.. ")
                print("Narrador: Espera! Escucho algo detras nuestro")
                print("*Narrador se da vuelta* (de alguna manera..) ")
                print("Narrador: Que es eso?.. OH NO! TENDREMOS QUE PELEAR!")
                pelear()
                bosquefirstfight = 1
                bosque()
            if bosquefirstfight == 1:
                print("En el medio del camino yace el cadaver de la criatura que acabas de asesinar")
                print("Fuera de eso, todo parace normal")
                bosque()
        if choice == 2:
            if bosquefirstfight == 0:
                global surprise

                print("TE ATACAN POR SORPRESA DESDE LA ESPALDA!")
                surprise = 1
                pelear()
                bosquefirstfight = 1
                bosque()
            viajar()
    bosque()
def pelear():
    FIGHTINSTANCE = 'false' # Corregir las mayusculas
    # print(BICHOS)
    def intropelea():
        global FIGHTINSTANCE
        global mob_puppet_vida
        global surprise
        print("entrando a intropelea()")
        if player.posicion == 1:
            mob = random.choice(creatures_bosque)
            print(mob)
        if player.posicion == 2:
            mob = random.choice(creatures_desierto)
            print(mob)
        print(creatures_bosque)
        print(creatures_desierto)
        print(mob)
        mob_puppet_vida = mob.vida
        print("puppet vida = ", mob_puppet_vida)
        print("Mob seleccionado: ", mob.nombre)
        print(f"Vida de {mob.nombre} = {mob.vida}")
        print(f"Daño de {mob.nombre} = {mob.ataque}")
        print(" ")
        print(f"Vida de {player.nombre} = {player.vida}")
        print(f"Daño de {player.nombre} = {player.ataque}")
        print(" ")

        def mobatack():
            print("Entrando a mobatack()")
            print(f"{mob.nombre} ataca y realiza {mob.ataque} de daño")
            player.vida = player.vida - mob.ataque
            print("vida del player: ", player.vida)
            if player.vida <= 0:
                print(f"{player.nombre} muere")
                print("saliendo de pelea, poniendo FIGHTINSTANCE = false")
                global FIGHTINSTANCE, Startfight
                FIGHTINSTANCE = 'false'
                Startfight = 0
                print(FIGHTINSTANCE)

        def playeratack():
            global mob_puppet_vida, surprise, FIGHTINSTANCE, startfight
            print(f"Narrador: {player.nombre}, tu turno de atacar!")
            print("Opcion 1 - Atacar")
            print("Opcion 2 - Intentar huir")
            choice = int(input("Eliges: ..  "))

            if choice == 1:
                print(f"{player.nombre} ataca y realiza {player.ataque} de daño")
                mob_puppet_vida = mob_puppet_vida - player.ataque
                print(f"Vida de {mob.nombre} = {mob_puppet_vida}")
            if choice == 2:
                print(f"{player.nombre} ataca y realiza {player.ataque} de daño")
                mob_puppet_vida = mob_puppet_vida - player.ataque
                print(f"Vida de {mob.nombre} = {mob_puppet_vida}")
            if mob_puppet_vida <= 0:
                print(f"{mob.nombre} muere")
                # print("saliendo de pelea, poniendo FIGHTINSTANCE = false")
                FIGHTINSTANCE = 'false'
                startfight = 0

                # print(FIGHTINSTANCE)

        def pelea():
            # print("Entrando a pelea()")
            global surprise
            if surprise == 1:
                mobatack()
            playeratack()
            if FIGHTINSTANCE == 'true':
                # print(FIGHTINSTANCE)
                mobatack()
            else:
                print("La pelea termino")

        while FIGHTINSTANCE == 'true':
            pelea()

    def startfight():
        # print("Entrando a startfight(): ")
        global startfight, FIGHTINSTANCE
        startfight = int(input("Empezar pelea, presiona 1: ... "))
        if startfight == 1:
            FIGHTINSTANCE = 'true'
            intropelea()

    startfight()
def viajar():
    mapa = ['Ciudad', 'Bosque', 'Desierto']
    if firsttimedesert == 0:
        mapa[2] = 'Adentrarse aun más en el bosque'
    if firsttimedesert == 1:
        mapa[2] = 'Estepa Desertica'
    if player.posicion > 0:
        print(f"<-- Volver a {mapa[player.posicion -1]} - Opcion 1")
    if player.posicion < 2:
        print(f"Viajar a {mapa[player.posicion +1]} --> - Opcion 2")
    print(f"Quedarse en {mapa[player.posicion]} - Opcion 3")
    choice = int(input("Opcion:.. "))
    if choice == 1:
        player.posicion = player.posicion - 1
    if choice == 2:
        player.posicion = player.posicion + 1
    if choice == 3:
        player.posicion = player.posicion
    map_init = [main_ciudad, main_bosque, main_desierto]
    map_init[player.posicion]()
def startgame():
    global clear
    print("- COMENZAR JUEGO - 1.")
    print("- SALIR - 2")
    choice = int(input("Opcion: .."))
    if choice == 1:
        print("Bienvenidx aventurerx a esta aventura sobre texto!")
        print("Mi nombre es {NOMBRE_GENERICO_ALGO_PRETENCIOSO} y te acompañare durante toda tu lectura")
        # El narrador esta pasando por un divorcion y
        # de vez en cuando hace comentarios sobre que extraña a su ex esposa llamada Laura.
        print("Cuentame un poco sobre ti, ¿Como te llamas?")
        player.nombre = input(f"{player.nombre}: Mi nombre es.. ")
        print(f"Gusto en conocerte {player.nombre}! ")
        print("Comencemos!")
        print(clear)
        print("*Breve explicacion del universo del juego y lleva al player a la ciudad principal*")
        main_ciudad()
    else:
        return
clear = "\n" * 100
player = Player('noname', 40, 5, 1, 0, 0)
questtracker = 0
bosquefirstfight = 0
surprise = 0
firsttimedesert = 0

# Indexado de criaturas
# dumy = Creatures('Dumy',1 ,1 ,1)
moblist = pd.read_table('creatures.txt', header=None, sep=',')
datalist = np.array(moblist)
# print(datalist)
creaturedata = []
creatures_bosque = []
creatures_desierto = []
a = 0
for x in range(len(datalist)-1):
    a = a+1
    # print("datalist: ", datalist[a])
    # print("datalist: ", datalist[a][0])
    datalist[a][0] = Creatures(datalist[a][0], int(datalist[a][1]), int(datalist[a][2]), int(datalist[a][3]), 0)
    creaturedata.append(datalist[a][0])
# Clasificacion de criaturas tipo bosque o desierto
a = 0
for x in range(len(creaturedata)):
    a = a+1
    #print("estoy aca")
    if creaturedata[a-1].tipo == 0:
        creatures_bosque.append(creaturedata[a-1])
        # print(f"Criatura {creaturedata[a-1].nombre} agregada a bosque")
    if creaturedata[a-1].tipo == 1:
        creatures_desierto.append(creaturedata[a-1])
        # print(f"Criatura {creaturedata[a-1].nombre}  agregada a desierto")

startgame()
# pelear()
