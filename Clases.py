class Player:
    def __init__(self, nombre, vida, ataque, defensa, atributo):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque  # daño fisico total
        self.defensa = defensa
        self.atributo = atributo  #reservado para efectos elementales o demas, queseyo jaja
        #poner en atributo = 0


class Bichos:
    def __init__(self, nombre, vida, daño, atributo):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
        self.atributo = atributo #reservado para caracteristicas especiales (corrupto, enfermo, venenoso etc..)


class Objeto_consumible:
    def __init__(self,nombre, cantidad, atributo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.atributo = atributo #reservado para tipo de efecto ej: curaciones


class Armas:
    def __init__(self, nombre, daño, tipo, atributo):
        self.nombre = nombre
        self.daño = daño
        self.tipo = tipo # 0 para armas de 1 mano, 1 para dos manos
        self.atributo = atributo # reservado para daño de elementos (fuego hielo veneno etc..)
        #daño normal -> atributo = o


class Escudos:
    def __init__(self, nombre, defensa, atributo):
        self.nombre = nombre
        self.defensa = defensa
        self.atributo = atributo #0 para fisico, 1 para magico


class Armaduras:
    def __init__(self, nombre, defensa, lugar, atributo):
        self.nombre = nombre
        self.defensa = defensa
        self.lugar = lugar   # 0 cabeza , 1 pecho , 2 brazos, 3 piernas
        self.atributo = atributo   # 0 para fisico, 1 para magico