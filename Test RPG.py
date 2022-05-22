import random
from time import sleep

import time

clear = "\n" * 100
PlayerStats = [10,2]
LoboStats = [5,2]
PlayerName = "NOMBRE"
MUNDO = ['Ciudad Capital', 'Bosque de Leñadores', 'Profundidades del bosque', 'Bosque de Leñadores']
cursor = 0
PlayerPos = MUNDO[cursor]
list = ' '
EventoBosque = 1
def CiudadPrincipal():
    print(clear)
    print(f"Bienvenido a {MUNDO[0]}!")
    print("Aqui encontraras muchas actividades para realizar!")
    def CiudadMain():
        print("Que Deseas hacer?")
        print("Mapa de Viaje - Opcion 1")
        print("Recorrer los suburbios - Opcion 2")
        PlayerChoice = int(input("Tu opcion es: "))
        print(clear)
        if PlayerChoice == 1:
            print(" Alla vamos!")
            MapNavigation(cursor = 0)
        if PlayerChoice == 2:
            print("Suburbios")
            CiudadPrincipal()
    CiudadMain()
def Bosque1():
    print(clear)
    print(f"Te diriges hacia{MUNDO[1]} ")
    def bosquemenu():
        print("Que deseas hacer .. ")
        print("Mapa de Viaje - 1")
        print("Investigar Bosque de Leñadores - 2")
        PlayerChoice = int(input("Opcion: "))
        print(clear)
        if PlayerChoice == 1:
            MapNavigation(cursor = 1)
        if PlayerChoice == 2:
            bosque1()
    def bosque1():
        print("No encuentras Nada")
        bosquemenu()
    bosquemenu()
def Bosque2():
    print(clear)
    print("Te adentras en las Profundidades del bosque..")
    if EventoBosque == 1:
        print(clear)
        print("CIUDADO!")
        print("ERES ATACADO POR SORPRESA POR UN LOBO!")
        print("RAPIDO! HAZ ALGO!")
        def pelea():

            def PlayerAtack():
                print("Tu turno de actuar!")
                print("Atacar - Opcion 1")
                print("Intentar huir - HUIR NUNCA ES UNA OPCION")
                PlayerChoice = int(input("Opcion: "))
                if PlayerChoice == 1:
                    LoboStats[0] = int(LoboStats[0] - PlayerStats[1])
                    print(f"Lobo recibe {PlayerStats[1]} de daño")
                    LoboAtack()


            def LoboAtack():
                print("Esquivar - Opcion 1")
                print("Contraatacar - Opcion 2")
                print("Bloquear - Opcion 3")
                PlayerChoice = int(input(" Opcion: "))
                if PlayerChoice == 1:
                    Esquivar = [0,1]
                    succes = int(random.choice(Esquivar))

                    if succes == 1:
                        print("Esquivas con Exito!")

                    if succes == 0:
                        print("No logras esquivar el ataque!")
                        PlayerStats[0] = [PlayerStats[0] - LoboStats[1]]
                        print(f"Lobo te hace {LoboStats[1]} de daño!")
                        print(f"Tu vida actual es: {PlayerStats[0]} ")
                        print(f"La vida de lobo es de: {LoboStats[0]} ")
                    PlayerAtack()



                if PlayerChoice == 2:
                    print("Contratacas como todo un ESPARTAANOO!!")

                    PlayerStats[0] = [PlayerStats[0] - LoboStats[1]]
                    print(f"Lobo te hace {LoboStats[1]} de daño!")
                    print(f"Dañas a Lobo por {PlayerStats[1]}")
                    LoboStats[0] = [LoboStats[0] - PlayerStats[1]]
                    print(f"Tu vida actual es: {PlayerStats[0]} ")
                    print(f"La vida de lobo es de: {LoboStats[0]} ")
                    PlayerAtack()

                if PlayerChoice == 3:
                    print("Intentas bloquear el ataque como puedes..")
                    bloquear = ['la cara', 'los brazos', 'la chota', 'el culo']
                    print(f"Lobo ataca y lo bloqueas con {random.choice(bloquear)}")
                    print("Logras bloquear 1 de daño proveniente de Lobo")

                    PlayerStats[0] = int(PlayerStats[0] - LoboStats[1] + 1)
                    print(f"Lobo te hace {LoboStats[1] -1} de daño!")
                    print(f"Tu vida actual es: {PlayerStats[0]} ")
                    print(f"La vida de lobo es de: {LoboStats[0]} ")
                    PlayerAtack()
            LoboAtack()

            if PlayerStats[0] == '0':
                print("Mueres a causa de las graves heridas..")
            if LoboStats[0] == '0':
                print("Lobo muere a causa de las graves heridas..")
                print("GANASTEE!")

        pelea()

    if EventoBosque == 0:
        def bosquemenu():
            print("Que deseas hacer .. ")
            print("Mapa de Viaje - 1")
            print("Investigar Bosque 2 - 2")
            PlayerChoice = int(input("Opcion: "))
            print(clear)
            if PlayerChoice == 1:
                MapNavigation(cursor)
            if PlayerChoice == 2:
                bosque2()

        def bosque2():
            print("bosque2")
            bosquemenu()

        bosquemenu()
def Bosque3():
    print(clear)
    print("Te encuentras en Bosque 3")

    def bosquemenu():
        print("Que deseas hacer .. ")
        print("Mapa de Viaje - 1")
        print("Investigar Bosque 3 - 2")
        PlayerChoice = int(input("Opcion: "))
        print(clear)
        if PlayerChoice == 1:
            MapNavigation()
        if PlayerChoice == 2:
            bosque3()

    def bosque3():
        print("bosque3")
        bosquemenu()

    bosquemenu()

def MapNavigation(cursor):
    print(clear)
    list = 'true'
    while list == 'true':
        print(" ")
        print(f"{MUNDO[cursor-1]} Opcion 1")
        print(f"{MUNDO[cursor]} Opcion 2")
        print(f"{MUNDO[cursor +1]} Opcion 3")
        MapSelection = input("Donde deseas ir:  ")

        if MapSelection == '1':
            list = 'false'
            cursor = cursor -1
            if cursor == len(MUNDO):
                cursor = 0
            if cursor == -len(MUNDO):
                cursor = 0
            PlayerPos = MUNDO[cursor]
            if PlayerPos == MUNDO[0]:
                CiudadPrincipal()
            if PlayerPos == MUNDO[1]:
                Bosque1()
            if PlayerPos == MUNDO[2]:
                Bosque2()
            if PlayerPos == MUNDO[3]:
                Bosque1()
        if MapSelection == '2':
            list = 'false'
            cursor = cursor
            if cursor == len(MUNDO):
                cursor = 0
            if cursor == -len(MUNDO):
                cursor = 0
            PlayerPos = MUNDO[cursor]
            if PlayerPos == MUNDO[0]:
                CiudadPrincipal()
            if PlayerPos == MUNDO[1]:
                Bosque1()
            if PlayerPos == MUNDO[2]:
                Bosque2()
            if PlayerPos == MUNDO[3]:
                Bosque3()
        if MapSelection == '3':

            list = 'false'
            cursor = cursor +1
            if cursor == len(MUNDO):
                cursor = 0
            if cursor == -len(MUNDO):
                cursor = 0
            PlayerPos = MUNDO[cursor]
            if PlayerPos == MUNDO[0]:
                CiudadPrincipal()
            if PlayerPos == MUNDO[1]:
                Bosque1()
            if PlayerPos == MUNDO[2]:
                Bosque2()
            if PlayerPos == MUNDO[3]:
                Bosque3()


def inicio():
    print("Entrar a Ciudad Principal - Opcion 1")
    print("Mapa de viaje - Opcion 2")
    PlayerChoice = int(input("Opcion: "))
    if PlayerChoice == 1:
        CiudadPrincipal()
    if PlayerChoice == 2:
        MapNavigation(cursor)
inicio()




