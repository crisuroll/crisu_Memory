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
        print("WELCOME TO MEMORY GAME!")
        self.tablero = None
        self.modo = None
        self.jugadores = []

    '''
    start() method. initializes the board and calls play() to start the game.
    '''
    def start(self):
        print("First, you must choose the board size. Minimum: 2x2. Maximum: 6x5 (also valid 5x6).")
    
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
        print("1. PLAYER 1 vs PLAYER 2 \n2. PLAYER vs CPU \n3. CPU vs CPU")
        self.modo = int(input("\nPlease choose a game mode: "))

        match self.modo:
            case 1:
                self.jugadores.append(Player(input("Enter PLAYER 1 name: ")))
                self.jugadores.append(Player(input("Enter PLAYER 2 name: ")))
            case 2:
                self.jugadores.append(Player(input("Enter PLAYER name: ")))
                print("1. EASY \n2. MEDIUM \n3. HARD \n4. EXPERT")
                nivel = int(input("Please choose the CPU level: "))
                cpu = Player("CPU", nivel)
                cpu.elegir_cartas(self.tablero)
                self.jugadores.append(cpu)
            case 3:
                print("1. EASY \n2. MEDIUM \n3. HARD \n4. EXPERT")
                nivel = int(input("Please choose both CPU levels: "))
                self.jugadores.append(Player("CPU 1", nivel))
                self.jugadores.append(Player("CPU 2", nivel))
            case _:
                print("Invalid option.")

    '''
    method choose(). receives the board and which card are they choosing (first or second of their turn).
    asks the player to choose which card they want to flip. first, it asks the row and then the column.
    '''
    def pedir_coordenadas(self, tablero, turno, jugador):
        while True:
            try:
                if jugador.nivel == 0:
                    f = int(input(f"Choose the row for the {turno} card: ")) - 1
                    c = int(input(f"Choose the column for the {turno} card: ")) - 1

                if f < 0 or f >= tablero.filas or c < 0 or c >= tablero.columnas:
                    print("Coords out of range. Please try again.")
                elif tablero.estaMostrado(f, c):
                    print("Card already flipped. Please choose another one.")
                else:
                    return f, c
            
            except ValueError:
                print("Error: Enter valid numbers.")

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
            print(f"\n{jugador.getName()}'S TURN")
        
            if jugador.nivel == 0: # Jugador
                f1, c1 = self.pedir_coordenadas(tablero, "first", jugador)
                tablero.mostrar(f1, c1)
                tablero.mostrarOculto()
                f2, c2 = self.pedir_coordenadas(tablero, "second", jugador)
                tablero.mostrar(f2, c2)
                tablero.mostrarOculto()
            else: # CPU
                f1, c1 = jugador.elegir_cartas(tablero)
                print(f"{jugador.getName()}'s first card is {f1 + 1}, {c1 + 1}:")
                tablero.mostrar(f1, c1)
                tablero.mostrarOculto()
                if jugador.nivel >= 2:
                    jugador.recordar_carta(f1, c1, self.tablero.tablero_parejas[f1][c1])
                time.sleep(2)
                f2, c2 = jugador.elegir_cartas(tablero)
                print(f"{jugador.getName()}'s second card is {f2 + 1}, {c2 + 1}:")
                tablero.mostrar(f2, c2)
                tablero.mostrarOculto()
                if jugador.nivel >= 2:
                    jugador.recordar_carta(f2, c2, self.tablero.tablero_parejas[f2][c2])
                time.sleep(2)

            if tablero.comprobar(f1, c1, f2, c2):
                print("Correct! You made a pair.")
                aciertos_actuales += 1
                jugador.setScore()
            else:
                print("You failed...")
                tablero.ocultar(f1, c1)
                tablero.ocultar(f2, c2)
                turno = 2 if turno == 1 else 1

            print(f"{j1.getName()}'s score: {j1.getScore()} - {j2.getName()}'s score: {j2.getScore()}")
            time.sleep(2)

        print("\nGame finished!")
        if j1.score > j2.score:
            print(f"{j1.name} wins with {j1.score} points!")
        elif j2.score > j1.score:
            print(f"¡{j2.name} wins with {j2.score} points!")
        else:
            print(f"It's a tie! Both players have {j1.score} points.")