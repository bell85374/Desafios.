import random

nombre = input("Nombre de tu heroe: ")
hp = 100
nivel = 1
xp = 0
oro = 50

inventario = ["espada", "pocion"]

print("\nBienvenido", nombre, "comienza tu aventura")

def mostrar_estado():
    print("\nESTADO")
    print("HP:", hp)
    print("Nivel:", nivel)
    print("XP:", xp)
    print("Oro:", oro)
    print("Inventario:", inventario)

def subir_nivel():
    global nivel, xp, hp
    if xp >= nivel * 50:
        nivel += 1
        xp = 0
        hp += 20
        print("\nSubiste al nivel", nivel)

def curar():
    global hp
    if "pocion" in inventario:
        hp += 30
        inventario.remove("pocion")
        print("Usaste una pocion y recuperaste 30 HP")
    else:
        print("No tienes pociones")

def encontrar_tesoro():
    global oro

    monedas = random.randint(10, 40)
    oro += monedas
    print("Encontraste", monedas, "monedas")

    if random.randint(1,3) == 1:
        inventario.append("pocion")
        print("Tambien encontraste una pocion")

def tienda():
    global oro

    print("\nTIENDA")
    print("1 Comprar pocion (20 oro)")
    print("2 Salir")

    opcion = input("> ")

    if opcion == "1":
        if oro >= 20:
            oro -= 20
            inventario.append("pocion")
            print("Compraste una pocion")
        else:
            print("No tienes suficiente oro")

def enemigo():
    global hp, xp, oro

    enemigo_hp = random.randint(30, 60) + (nivel * 5)

    print("\nUn monstruo aparece")

    while enemigo_hp > 0 and hp > 0:

        print("\n1 Atacar")
        print("2 Curar")

        accion = input("> ")

        if accion == "1":
            dano = random.randint(10, 25) + (nivel * 2)
            enemigo_hp -= dano
            print("Hiciste", dano, "de dano")

        elif accion == "2":
            curar()

        if enemigo_hp > 0:
            dano = random.randint(5, 15)
            hp -= dano
            print("El enemigo te golpea por", dano)

    if hp > 0:
        recompensa_xp = random.randint(20, 40)
        recompensa_oro = random.randint(10, 30)

        xp += recompensa_xp
        oro += recompensa_oro

        print("Ganaste", recompensa_xp, "XP")
        print("Ganaste", recompensa_oro, "oro")

        subir_nivel()

while hp > 0:

    print("\nMENU")
    print("1 Explorar")
    print("2 Ver estado")
    print("3 Usar pocion")
    print("4 Tienda")
    print("5 Salir")

    opcion = input("> ")

    if opcion == "1":

        evento = random.choice(["enemigo", "tesoro", "nada"])

        if evento == "enemigo":
            enemigo()

        elif evento == "tesoro":
            encontrar_tesoro()

        else:
            print("Caminaste por el bosque")

    elif opcion == "2":
        mostrar_estado()

    elif opcion == "3":
        curar()

    elif opcion == "4":
        tienda()

    elif opcion == "5":
        print("Fin del juego")
        break

if hp <= 0:
    print("Has sido derrotado. Fin del juego")
