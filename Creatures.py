import random
import pandas as pd
import numpy as np

class Creatures:
    def __init__(self, nombre, vida, ataque, tipo):
        print("criatura agregada a clase Creatures")
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo

# dumy = Creatures('Dumy',1 ,1 ,1)
moblist = pd.read_table('creatures.txt', header=None, sep=',')
datalist = np.array(moblist)
print(datalist)
creaturedata = []
creatures_bosque = []
creatures_desierto = []
a = 0
for x in range(len(datalist)-1):
    a = a+1
    # print("datalist: ", datalist[a])
    # print("datalist: ", datalist[a][0])
    datalist[a][0] = Creatures(datalist[a][0], int(datalist[a][1]), int(datalist[a][2]), int(datalist[a][3]))
    creaturedata.append(datalist[a][0])
a = 0

# print(creaturedata[0].tipo)
for x in range(len(creaturedata)):
    a = a+1
    #print("estoy aca")
    if creaturedata[a-1].tipo == 0:
        creatures_bosque.append(creaturedata[a-1])
        print(f"Criatura {creaturedata[a-1].nombre} agregada a bosque")
    if creaturedata[a-1].tipo == 1:
        creatures_desierto.append(creaturedata[a-1])
        print(f"Criatura {creaturedata[a-1].nombre}  agregada a desierto")

print(creatures_bosque[0].nombre)
print(creatures_desierto)