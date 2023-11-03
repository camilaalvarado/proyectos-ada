
# Proyecto Integrador parte 4

#1. Implementar una función que reciba el mapa de un laberinto en forma de cadena
# y lo convierta a matriz de caracteres
#2. Escribir una función que limpie la pantalla y muestre la matriz (recibe el mapa en forma de matriz)
#3. Implementar el main loop en una función (recibe el mapa en forma de matriz)


import os
from readchar import readkey,key

def convertir_laberinto(laberinto):
    for fila in laberinto.split("\n"):
        print(list(fila))
    return [list(fila) for fila in laberinto.split("\n")]

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mapa(mapa):
    for fila in mapa:
        print(''.join(fila))

def main_loop(mapa, posicion_inicial, posicion_final):
    px, py = posicion_inicial

    while (px, py) != posicion_final:
        limpiar_pantalla()
        mapa[px][py] = 'P'
        mostrar_mapa(mapa)
        mapa[px][py] = '.'

        tecla = readkey()
        if tecla == key.UP and px > 0 and mapa[px - 1][py] != '#':
            px -= 1  # Arriba
        elif tecla == key.DOWN and px < len(mapa) - 1 and mapa[px + 1][py] != '#':
            px += 1  # Abajo
        elif tecla == key.LEFT and py > 0 and mapa[px][py - 1] != '#':
            py -= 1  # Izquierda
        elif tecla == key.RIGHT and py < len(mapa[0]) - 1 and mapa[px][py + 1] != '#':
            py += 1  # Derecha
    print ("Has llegado a la meta !!Ganaste!!")


laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = convertir_laberinto(laberinto)
posicion_inicial = (0, 0)
posicion_final = (len(mapa) - 1, len(mapa[0]) - 1)
main_loop(mapa, posicion_inicial, posicion_final)