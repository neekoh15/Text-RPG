import random
import pandas as pd
import numpy as np
import sys
import time

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
        self.atributo = atributo

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
# print_slow(" test ")
def main_ciudad():
    global queststatus
    print(" ")
    print("- Entrando a ciudad principal -")
    print(" ")
    if queststatus[0] == 1:
        print(" - QUEST TERMINADA - Viajar a la ciudad")
        queststatus[0] = 2
    def ciudad():
        print(" ")
        print(" Opciones: ")
        print("- Recorrer la ciudad - 1: ")
        print("- Mapa de Viaje - 2: ")
        choice = int(input(" Tu opcion: .. "))
        if choice == 1:
            print("- Investigar la ciudad -")
            print(" ")
            print("-- PROXIMAMENTE -- ")
            print("- Academias -")
            print("- Barracas -")
            print("- Mercader -")
            print("- Taberna -")
            print("- Alquimista - ")
            print(" ")
            ciudad()

        if choice == 2:
            viajar()
    ciudad()
def main_pueblo():
    # print(f"Bienvenido a Pueblo Inicial!")
    print("- Pueblo Inicial -")
    # print("Aqui encontraras muchas actividades para realizar!")
    def ciudad():
        print(" ")
        # Proximas cosas a agregar: Taberna (Quests aca) - Barracas -(Aprender Clase) - Alquimista (Pociones) - Herrero (Armaduras y armas)
        print("- Recorrer el pueblo - 1")  # Investigar permitiria encontrar items y quest especiales (?
        print("- Vistar al curandero - 2")
        # if questtracker == 0:
          #  print("Irse - 3")
        # if questtracker == 1:
          #  print("Irse - 3")
        print("- Mapa de viaje - 3")
        choice = int(input("Opcion:.. "))
        global queststatus
        if choice == 1:
            print(" ")
            print("- Descripcion del lugar - ")
            if queststatus[0] == 0:
                print(" ")
                print("- Volver - Opcion 1: ")
                print("- Quest Inicial - 2: ")
                """print("Excepto por un pequeño niño sentado en uno de los bancos, llorando..")
                print("Dejar de fizgonear y ocuparme de mis asuntos - 1")
                print("Acercarse al pequeño niño - 2")"""
                choice = int(input(f"Narrador: {player.nombre}, que quieres hacer?: .. "))
                if choice == 1:
                    ciudad()
                if choice == 2:
                    print(" ")
                    # print("Te acercas al niño y te cuenta sus problemas, por algun motivo..")
                    # print("- QUEST ACEPTADA - {Encuentrar la familia del niño lloron}")
                    print(" - QUEST ACEPTADA - ")
                    print("Mision : Viajar a la ciudad")
                    queststatus[0] = 1
                    ciudad()
            if queststatus[0] == 1:
                print("- Volver a atras -")
                ciudad()


        if choice == 2:
            if player.vida == 40:
                print(" ")
                print("Curandero: Quien se atreve a interrumpir mis actividades!?")
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
    global mapainfo
    def desierto():
        global surprise
        event = np.random.choice(np.arange(0, 2), p=[1.0, 0.0])
        print(" ")
        print("- Te encuentra en el desierto -")
        print(" ")
        print("Investigar el lugar - 1")
        print("Continuar viajando - 2")
        choice = int(input("Opcion:.. "))
        if choice == 1:
            if event == 1:
                print(" ")
                print("Narrador : Algo se mueve detras de esas dunas!")
                print("Narrador: Cuidado! Tendremos que pelear!")
                print(" ")
                pelear()
            if event == 0:
                print(" ")
                print("- Descripcion del lugar -")
            desierto()
        if choice == 2:
            if event == 1:
                print("A pelear!")
                surprise = 1
                pelear()
            if event == 0:
                print("- Mapa de viaje -")
                viajar()
    print(" ")
    if mapainfo[2] == 0:
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
            print("Breve descripcion del paisaje e introduccion al desierto")
            mapainfo[2] = 1
            desierto()
    if mapainfo[2] == 1:
        desierto()


    """if mapainfo[2] == 0:
         print(" - Primera vez en el desierto -")
        # print("El desierto es un lugar peligroso, lleno de bandidos y criaturas extrañas, sera mejor viajar con cautela..")
         mapainfo[2] == 1"""
    if mapainfo[2] == 1:
        print("Te encuentra en el desierto")


    desierto()
def main_bosque():
    print(" ")
    print("Te adentras en las profundidades del bosque.. ")
    def bosque():
        global surprise
        event = np.random.choice(np.arange(0, 2), p=[1.0, 0.0])
        print(event)
        if a == 'False':
            event = 0
        if event == 1:
            print(" Escuchas algo ")
        print(" ")
        print(f"Narrador: {player.nombre}, que deseas hacer? ..")
        print("Investigar el lugar - 1")
        print("Continuar viajando - 2")
        print(" ")
        choice = int(input("Opcion:.. "))

        if choice == 1:
            print(" ")
            if event == 0:
                print("investigando bosque ..")
                bosque()
            if event == 1:
                print("- Descubre que te estaban por atacar y reaccionas a tiempo -")
                pelear()
            bosque()

        if choice == 2:
           if event == 0:
                print("- Mapa de Viaje -")
                viajar()
           if event == 1:
                print(" Te atacan por sorpresa")
                surprise = 1
                pelear()
                bosque()
    bosque()
def pelear():
    fightstance = 'false' # Corregir las mayusculas
    # print(BICHOS)
    def intropelea():
        global fightstance, mob_puppet_vida, surprise, mapaactual
        # print("entrando a intropelea()")
        if mapaactual == 'Bosque':
            mob = random.choice(creatures_bosque)
            # print(mob)
        if mapaactual == 'Desierto':
            mob = random.choice(creatures_desierto)
            # print(mob)
        # print(creatures_bosque)
        # print(creatures_desierto)
        # print(mob)
        mob_puppet_vida = mob.vida
        # print("puppet vida = ", mob_puppet_vida)
        print(" ")
        print("Mob seleccionado: ", mob.nombre)
        print(f"Vida de {mob.nombre} = {mob.vida}")
        print(f"Daño de {mob.nombre} = {mob.ataque}")
        print(" ")
        print(f"Vida de {player.nombre} = {player.vida}")
        print(f"Daño de {player.nombre} = {player.ataque}")
        print(" ")

        def mobatack():

            global fightstance, Startfight, surprise
            # print("Entrando a mobatack()")
            if surprise == 1: # El golpe por sorpresa no es esquivable ni defendible
                print(" ")
                print(f"{mob.nombre} te ataca por sorpresa")
                print(f"{mob.nombre} ataca y realiza {mob.ataque} de daño")
                player.vida = player.vida - mob.ataque
                print("vida del player: ", player.vida)
                surprise = 0
                playeratack()
            if surprise == 0: # Player puede intentar defender, esquivar o contratacar
                print(" ")
                print("Es el turno de tu oponente!")
                print(f"{mob.nombre} intenta atacarte!")
                print(" ")
                print("Intentar bloquear el ataque - Opcion 1")
                print("Intentar Esquivar el ataque - Opcion 2")
                print("Intentar Contratacar - Opcion 3")
                player_choice = int(input("- Opcion: .. "))
                # Bloquear
                if player_choice == 1:
                    print("Intentas bloquear el ataque y.. ")
                    succes = random.choice([0,1,2])
                    if succes == 0: # Fallo
                        print("Bloqueas torpemente pero logras mitigar algo de daño..")
                        print("Bloqueas 1 de daño")
                        player.vida = player.vida - mob.ataque + 1
                        print(f"{mob.nombre} te realiza {mob.ataque -1} de daño ")
                        print("vida del player: ", player.vida)
                    if succes == 1: # Exito
                        print("Bloqueas exitosamente el ataque!")
                        print(f"Daño bloqueado: {mob.ataque}")
                    if succes == 2: # Fallo critico
                        print("Breve Recap.. ")
                        print("Nunca fuiste el más listo en el colegio.. De hecho, nunca fuiste listo del todo")
                        print("Tus mismos padres te lo decian, tu fuerte no es eso de pensar..")
                        print("En fin..")
                        print("Tus super instintos de guerrero nato (*Coff* *Coff*) se apoderan de ti y..")
                        print("Intentas de bloquear el ataque con.. La cara!")
                        print(f"Lo que ocasiona que el golpe de {mob.nombre} sea CRITICO")
                        player.vida = player.vida - mob.ataque*2.5
                        print(f"{mob.nombre} realiza {mob.ataque*2.5} de daño")
                        print("vida del player: ", player.vida)
                # Esquivar
                if player_choice == 2:
                    succes = random.choice([0,1])
                    if succes == 0: # Fallas
                        print(f"Intentas esquivar y no lo logras, {mob.nombre} alcanza a golpearte en el ultimo instante")
                        player.vida = player.vida - mob.ataque
                        print(f"{mob.nombre} te realiza {mob.ataque} de daño")
                    if succes == 1: # Aciertas
                        print("Esquivas exitosamente el ataque!")
                        playeratack()
                # Contratacar
                if player_choice == 3:
                    global mob_puppet_vida, startfight
                    print("Contratacas!")
                    mob_puppet_vida = mob_puppet_vida - player.ataque
                    print(f"{mob.nombre} recibe {player.ataque} de daño")
                    if mob_puppet_vida <= 0:
                        print(f"{mob.nombre} muere")
                        # print("saliendo de pelea, poniendo FIGHTINSTANCE = false")
                        fightstance = 'false'
                        startfight = 0
                        surprise = 0
                    else:
                        player.vida = player.vida - mob.ataque
                        print(f"{mob.nombre} realiza {mob.ataque*1.5} de daño")
            if player.vida <= 0:
                print(f"{player.nombre} muere")
                # print("saliendo de pelea, poniendo FIGHTINSTANCE = false")

                fightstance = 'false'
                Startfight = 0
                muerte()
                # print(fightstance)

        def playeratack():
            print(" ")
            global mob_puppet_vida, surprise, fightstance, startfight
            print(f"Narrador: {player.nombre}, tu turno de atacar!")
            print(" ")
            print("Opcion 1 - Atacar")
            print("Opcion 2 - Intentar huir")
            choice = int(input("Eliges: ..  "))

            if choice == 1:
                print(" ")
                print(f"{player.nombre} ataca y realiza {player.ataque} de daño")
                mob_puppet_vida = mob_puppet_vida - player.ataque
                print(f"Vida de {mob.nombre} = {mob_puppet_vida}")
            if choice == 2:
                print(" ")
                print(f"Narrador: {player.nombre} huyamos de aqui!")
                print("Intetas huir y.. ")
                huir = random.choice([0,1])
                if huir == 0:
                    print(" ")
                    print("De repente tropiezas en el camino..")
                    print(f"{mob.nombre} se avalanza rapidamente sobre ti!")
                    mobatack()
                if huir == 1:
                    print(" ")
                    print("Lo consigues!")
                    print("- Huyes de la batalla -")
                    fightstance = 'false'
            if mob_puppet_vida <= 0:
                print(" ")
                print(f"{mob.nombre} muere")
                # print("saliendo de pelea, poniendo FIGHTINSTANCE = false")
                fightstance = 'false'
                startfight = 0
                surprise = 0
                # print(FIGHTINSTANCE)

        def pelea():
            # print("Entrando a pelea()")
            global surprise
            if surprise == 1:
                mobatack()
            playeratack()
            if fightstance == 'true':
                # print(FIGHTINSTANCE)
                mobatack()
            else:
                print("La pelea termino..")

        while fightstance == 'true':
            pelea()

    def startfight():
        # print("Entrando a startfight(): ")
        global startfight, fightstance
        startfight = int(input("Empezar pelea, presiona 1: ... "))
        if startfight == 1:
            fightstance = 'true'
            intropelea()
    startfight()
def muerte():
    print("Mueres, volviendo a empezar..")
    startgame()
def viajar():
    global mapainfo, mapaactual
    mapa = ['Pueblo', 'Bosque', 'Bosque','Bosque', 'Desierto', 'Desierto', 'Desierto', 'Ciudad Capital']
    # mapainfo = [1, 0, 0, 0] # pueblo, bosque, desierto, ciudad - 0 para no descubierto, 1 para descubierto
    # bosque = [1, 2, 3]
    # desierto= [1, 2, 3]
    # if mapainfo[2] == 0: # Indicadores de primera visita
        # mapa[2] = 'Adentrarse aun más en el bosque'
    # if mapainfo[2] == 1: # Lugar descubierto, por el momento deshabilitado
        # mapa[2] = 'Estepa Desertica'
    if player.posicion > 0:
        print(f"<-- Volver a {mapa[player.posicion -1]} - Opcion 1")
    if player.posicion < len(mapa)-1:
        print(f"Viajar a {mapa[player.posicion +1]} --> - Opcion 2")
    print(f"Quedarse en {mapa[player.posicion]} - Opcion 3")
    choice = int(input("Opcion:.. "))
    if choice == 1:
        player.posicion = player.posicion - 1
    if choice == 2:
        player.posicion = player.posicion + 1
    if choice == 3:
        player.posicion = player.posicion
    if player.posicion < 0: # Asi no me voy del Index
        player.posicion = 0
    if player.posicion > len(mapa): # Asi no me voy del Index
        player.posicion = len(mapa)
    # -------------- FUNCIONES DE VIAJE --------------------------------------------
    mapaactual = mapa[player.posicion]
    # map_init = [main_pueblo, main_bosque, main_desierto, main_ciudad] # llama a las funciones de los mapas
    if mapaactual == 'Pueblo':
        main_pueblo()
    if mapaactual == 'Bosque':
        main_bosque()
    if mapaactual == 'Desierto':
        main_desierto()
    if mapaactual == 'Ciudad Capital':
        main_ciudad()
    # map_init[player.posicion]() # activa las funciones de los mapas
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
        main_pueblo()
    else:
        return
clear = "\n" * 2
player = Player('noname', 40, 5, 1, 0, 0)
# playerstatus = [0,] ???
# questtracker = 0 # ya no se usa
queststatus = [0]
# bosquefirstfight = 0 # Reservado como para un tutorial o algo asi
surprise = 0
mapainfo = [1, 0, 0, 0]
mapaactual = 'Pueblo'
# Indexado de criaturas
# dumy = Creatures('Dumy',1 ,1 ,1) # Mob de prueba
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
