import random
import numpy as np
import pandas as pd


class Player:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque


class Creatures:
    def __init__(self, nombre, vida, ataque, tipo):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo

mobss = pd.read_csv("creatures2.txt")
moblist = np.array(mobss)
fightinstance = 'true'
mapaactual = ['Bosque']
mobseleccionado = [0]
player = Player('Player1', 999, 1)
dummy0 = Creatures('dummy0', 10, 1, 0)
dummy1 = Creatures('dummy1', 10, 1, 0)
dummy2 = Creatures('dummy2', 10, 1, 0)
dummy3 = Creatures('dummy3', 10, 1, 0)
mobs = []
creatures_bosque = []
mobs.append(dummy0)
mobs.append(dummy1)
mobs.append(dummy2)
mobs.append(dummy3)
def dummy0():
    print(" ")
    dummy0 = Creatures('dummy0', 10, 1, 0)
    print(f"Soy {dummy0.nombre} y te voy a atacar")
    print(f"{dummy0.nombre} ataque y te realiza {dummy0.ataque} de daño")
    playeratack()
def dummy1():
    print(" ")
    dummy1 = Creatures('dummy1', 10, 1, 0)
    print(f"Soy {dummy1.nombre} y te voy a atacar, con un texto diferente")
    print(f"{dummy1.nombre} ataque y te realiza {dummy1.ataque} de daño")
    playeratack()
def dummy2():
    print(" ")
    dummy2 = Creatures('dummy2', 10, 1, 0)
    print(f"Soy {dummy2.nombre} y te voy a atacar")
    print(f"{dummy2.nombre} ataque y te realiza {dummy2.ataque} de daño")
    playeratack()
def dummy3():
    print(" ")
    dummy3 = Creatures('dummy3', 10, 1, 0)
    print(f"Soy {dummy3.nombre} y te voy a atacar")
    print(f"{dummy3.nombre} ataque y te realiza {dummy3.ataque} de daño")
    playeratack()
for x in mobs:
    a = x.tipo
    if a == 0:
        creatures_bosque.append(x)

def playeratack():
    global fightinstance, mobseleccionado
    print("- playeratack() -")
    ataque = input(" Presiona cualquier tecla para atacar")
    print(f"{player.nombre} ataca y realiza {player.ataque} de daño")
    if mobseleccionado[0].vida == 0:
        fightinstance = 'false'
    else:
        pelear()

def pre_pelear():
    global mobseleccionado, fightinstance
    fightinstance = 'true'
    print(mapaactual[0])
    if mapaactual[0] == 'Bosque':
        mobseleccionado[0] = random.choice(creatures_bosque)
    print(mobseleccionado[0])
    print(f"{mobseleccionado[0].nombre} fue seleccionado")
    pelear()
def pelear():
    global mobseleccionado
    while fightinstance == 'true':
        mob_name = mobseleccionado[0].nombre  # set by the command line options
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(mob_name)
        method()


pre_pelear()