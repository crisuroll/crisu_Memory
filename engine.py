###################################################################
from player import Player
from board import Board
###################################################################


# COSAS QUE HACER AQUÍ
## Elegir dificultad (más adelante)
## Elegir modo de juego y crear jugadores con clase player
## funcion play para jugar, aqui pegar lo que tengo de main

# ## dificultades máquina MAS ADELANTE
# print("1. FÁCIL2 \n2. INTERMEDIO \n3. DIFÍCIL \n4. EXPERTO")
# lvl = int(input("\nElige la dificultad de la CPU: "))


def start():
    print("¡BIENVENIDO AL JUEGO MEMORY!")
    print("Primero debes indicar el tamaño del tablero. Mínimo: 2x2. Máximo: 6x5 (también válido 5x6).")
    
    filas, columnas = Board.pedir_dimensiones()
    tablero = Board(filas, columnas)
    
    print("TABLERO INICIAL:")
    tablero.mostrarOculto()
    
    print("1. JUGADOR 1 vs JUGADOR 2 \n2. JUGADOR vs CPU \n3. CPU vs CPU")
    modo = int(input("\nElige un modo de juego: "))
    play(tablero, modo)

def play(tablero, modo):
    match modo:
        case 1:
            j1 = Player(input("Introduce el nombre del jugador 1: "))
            j2 = Player(input("Introduce el nombre del jugador 2: "))
        case 2:
            j1 = Player(input("Introduce el nombre del jugador 1: "))
            j2 = Player.name = "CPU"
        case 3:
            j1 = Player.name = "CPU 1"
            j2 = Player.name = "CPU 2"

    turno = 1  # 1 = j1; 2 = j2
    aciertos_actuales = 0
    aciertos_totales = (tablero.filas * tablero.columnas) // 2

    while aciertos_actuales < aciertos_totales:
        jugador = j1 if turno == 1 else j2
        print(f"\nTURNO DE {jugador.name}")
        
        f1, c1 = pedir_coordenadas(tablero, "primera")
        tablero.mostrar(f1, c1)
        tablero.mostrarOculto()
        
        f2, c2 = pedir_coordenadas(tablero, "segunda")
        tablero.mostrar(f2, c2)
        tablero.mostrarOculto()

        if tablero.comprobar(f1, c1, f2, c2):
            print("¡Correcto! Has encontrado una pareja.")
            aciertos_actuales += 1
            jugador.score += 1
        else:
            print("Has fallado...")
            tablero.ocultar(f1, c1)
            tablero.ocultar(f2, c2)
            turno = 2 if turno == 1 else 1

        print(f"Puntaje {j1.name}: {j1.score} - Puntaje {j2.name}: {j2.score}")

    # Fin del juego y declaración del ganador
    print("\n¡Juego terminado!")
    if j1.score > j2.score:
        print(f"¡{j1.name} gana con {j1.score} puntos!")
    elif j2.score > j1.score:
        print(f"¡{j2.name} gana con {j2.score} puntos!")
    else:
        print("¡Es un empate!")

def pedir_coordenadas(tablero, turno):
    while True:
        try:
            f = int(input(f"Introduce la fila para la {turno} carta: ")) - 1
            c = int(input(f"Introduce la columna para la {turno} carta: ")) - 1

            if f < 0 or f >= tablero.filas or c < 0 or c >= tablero.columnas:
                print("Coordenadas fuera de rango. Inténtalo de nuevo.")
            elif tablero.estaMostrado(f, c):
                print("Carta ya descubierta. Elige otra.")
            else:
                return f, c
            
        except ValueError:
            print("Error: Introduce números válidos.")