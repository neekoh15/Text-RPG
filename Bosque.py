
def main_bosque():
    print("main bosque")
    print("Investigar - 1")
    print("Salir - 2")
    choice = int(input("Opcion:.. "))
    if choice == 1:
        print("investigando")
        startfight()
        main_bosque()
    if choice == 2:
        viajar()
