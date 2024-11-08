###################################################################
from player import Player
from board import Board
import time
###################################################################

class Engine:
    '''
    constructor.
    attributes board, mode.
    '''
    def __init__(self):
        print("¡BIENVENIDO AL JUEGO MEMORY!")
        self.tablero = None
        self.modo = None
        self.jugadores = []

    '''
    start() method. initializes the board and calls play() to start the game.
    '''
    def start(self):
        print("Primero debes indicar el tamaño del tablero. Mínimo: 2x2. Máximo: 6x5 (también válido 5x6).")
    
        filas, columnas = Board.pedir_dimensiones()
        self.tablero = Board(filas, columnas)
    
        print("TABLERO INICIAL:")
        self.tablero.mostrarOculto()
    
        self.config()

        self.play(self.tablero)

    '''
    config() method. sets the game mode and the difficult level.
    '''
    def config(self):
        print("1. JUGADOR 1 vs JUGADOR 2 \n2. JUGADOR vs CPU \n3. CPU vs CPU")
        self.modo = int(input("\nElige un modo de juego: "))

        match self.modo:
            case 1:
                self.jugadores.append(Player(input("Introduce el nombre del jugador 1: ")))
                self.jugadores.append(Player(input("Introduce el nombre del jugador 2: ")))
            case 2:
                self.jugadores.append(Player(input("Introduce el nombre del jugador 1: ")))
                print("1. FÁCIL \n2. INTERMEDIO \n3. DIFÍCIL \n4. EXPERTO")
                nivel = int(input("Elige la dificultad de la CPU: "))
                cpu = Player("CPU", nivel)
                cpu.elegir_cartas(self.tablero)
                self.jugadores.append(cpu)
            case 3:
                print("1. FÁCIL \n2. INTERMEDIO \n3. DIFÍCIL \n4. EXPERTO")
                nivel = int(input("Elige la dificultad de ambas CPU: "))
                self.jugadores.append(Player("CPU1", nivel))
                self.jugadores.append(Player("CPU2", nivel))
            case _:
                print("Opción no válida.")

    '''
    method choose(). receives the board and which card are they choosing (first or second of their turn).
    asks the player to choose which card they want to flip. first, it asks the row and then the column.
    '''
    def pedir_coordenadas(self, tablero, turno, jugador):
        while True:
            try:
                if jugador.nivel == 0:
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

    '''
    play method(). receives the board and the game mode.
    '''
    def play(self, tablero):
        j1 = self.jugadores[0]
        j2 = self.jugadores[1]
        turno = 1  # 1 = j1; 2 = j2
        aciertos_actuales = 0
        aciertos_totales = (tablero.filas * tablero.columnas) // 2

        while aciertos_actuales < aciertos_totales:
            jugador = j1 if turno == 1 else j2
            print(f"\nTURNO DE {jugador.getName()}")
        
            if jugador.nivel == 0: # Jugador
                f1, c1 = self.pedir_coordenadas(tablero, "primera", jugador)
                tablero.mostrar(f1, c1)
                tablero.mostrarOculto()
                f2, c2 = self.pedir_coordenadas(tablero, "segunda", jugador)
                tablero.mostrar(f2, c2)
                tablero.mostrarOculto()
            else: # CPU
                f1, c1 = jugador.elegir_cartas(tablero)
                print(f"{jugador.getName()} ha elegido como primera carta {f1 + 1}, {c1 + 1}:")
                tablero.mostrar(f1, c1)
                tablero.mostrarOculto()
                time.sleep(2)
                f2, c2 = jugador.elegir_cartas(tablero)
                print(f"{jugador.getName()} ha elegido como segunda carta {f2 + 1}, {c2 + 1}:")
                tablero.mostrar(f2, c2)
                tablero.mostrarOculto()
                time.sleep(2)

                if jugador.nivel >= 2:
                    jugador.recordar_carta(f1, c1, self.tablero.tablero_parejas[f1][c1])
                    jugador.recordar_carta(f2, c2, self.tablero.tablero_parejas[f2][c2])

            if tablero.comprobar(f1, c1, f2, c2):
                print("¡Correcto! Has encontrado una pareja.")
                aciertos_actuales += 1
                jugador.setScore()
            else:
                print("Has fallado...")
                tablero.ocultar(f1, c1)
                tablero.ocultar(f2, c2)
                turno = 2 if turno == 1 else 1

            print(f"Puntuación {j1.getName()}: {j1.getScore()} - Puntuación {j2.getName()}: {j2.getScore()}")
            time.sleep(2)

        print("\n¡Juego terminado!")
        if j1.score > j2.score:
            print(f"¡{j1.name} gana con {j1.score} puntos!")
        elif j2.score > j1.score:
            print(f"¡{j2.name} gana con {j2.score} puntos!")
        else:
            print("¡Es un empate!")