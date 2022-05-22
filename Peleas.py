import random


def pelear():
    fightstance = 'false' # Corregir las mayusculas
    # print(BICHOS)
    def intropelea():
        global fightstance
        global mob_puppet_vida
        global surprise
        # print("entrando a intropelea()")
        if player.posicion == 1:
            mob = random.choice(creatures_bosque)
            print(mob)
        if player.posicion == 2:
            mob = random.choice(creatures_desierto)
            print(mob)
        # print(creatures_bosque)
        # print(creatures_desierto)
        # print(mob)
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
            global fightstance, Startfight, surprise
            # print("Entrando a mobatack()")
            if surprise == 1: # El golpe por sorpresa no es esquivable ni defendible
                print(f"{mob.nombre} ")
                print(f"{mob.nombre} ataca y realiza {mob.ataque} de daño")
                player.vida = player.vida - mob.ataque
                print("vida del player: ", player.vida)
                surprise = 0
            if  surprise == 0: # Player se puede intentar defender, esquivar o contratacar
                print("Intentar bloquear el ataque - Opcion 1")
                print("Intentar Esquivar el ataque - Opcion 2")
                print("Intentar Contratacar - Opcion 3")
                player_choice = int(input("- Opcion: .. "))
                # Bloquear
                if player_choice == 0:
                    print("Intentas bloquear el ataque y.. ")
                    succes = random.choice(0,1,2)
                    if succes == 0: # Fallo
                        print("Bloqueas torpemente pero logras mitigar algo de daño..")
                        print("Bloqueas 1 de daño")
                        player.vida = player.vida - mob.ataque -1
                        print("vida del player: ", player.vida)
                    if succes == 1: # Exito
                        print("Bloqueas exitosamente el ataque!")
                        print(f"Daño bloqueado: {mob.ataque}")
                    if succes = 2: # Fallo critico
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
                if player_choice == 1:
                    succes = random.choice(0, 1)
                    if succes == 0: # Fallas
                         print(f"Intentas esquivar y no lo logras, {mob.nombre} alcanza a golpearte en el ultimo instante")
                        player.vida = player.vida - mob.ataque
                        print(f"{mob.nombre} te realiza {mob.ataque} de daño")
                    if succes == 1: # Aciertas
                        print("Esquivas exitosamente el ataque!")
                        playeratack()
                # Contratacar
                if player_choice == 2:
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
                        print(f"{mob.nombre} realiza {mob.ataque * 2.5} de daño")
            if player.vida <= 0:
                print(f"{player.nombre} muere")
                # print("saliendo de pelea, poniendo FIGHTINSTANCE = false")

                fightstance = 'false'
                Startfight = 0
                muerte()
                # print(fightstance)

        def playeratack():
            global mob_puppet_vida, surprise, fightstance, startfight
            print(f"Narrador: {player.nombre}, tu turno de atacar!")
            print("Opcion 1 - Atacar")
            print("Opcion 2 - Intentar huir")
            choice = int(input("Eliges: ..  "))

            if choice == 1:
                print(f"{player.nombre} ataca y realiza {player.ataque} de daño")
                mob_puppet_vida = mob_puppet_vida - player.ataque
                print(f"Vida de {mob.nombre} = {mob_puppet_vida}")
            if choice == 2:
                print(f"Narrador: {player.nombre} huyamos de aqui!")
                print("Intetas huir y.. ")
                huir = random.choice(0,1)
                if huir == 0:
                    print("De repente tropiezas en el camino..")
                    print(f"{mob.nombre} se avalanza rapidamente sobre ti!")
                    mobatack()
                if huir == 1:

                    print("Lo consigues!")
                    print("- Huyes de la batalla -")
                    fightstance = 'false'
            if mob_puppet_vida <= 0:
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
