###################################################################
import random
from player import Player
###################################################################

class Board:
    '''
    constructor. receives rows and columns.
    attributes rows, columns, hiddenBoard, pairsBoard, maxPoints
    '''
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero_oculto = []
        self.tablero_parejas = []
        self.max_points = (self.filas * self.columnas) // 2
        self.crear_tablero_oculto()
        self.crear_tablero_parejas()
        self.memory = []

    '''
    askSize() method. asks the user the number of rows and columns to create the board.
    '''
    def pedir_dimensiones():
        while True:
            try:
                filas = int(input("Please enter the number of rows: "))
                columnas = int(input("Please enter the number of columns: "))
                if (filas < 2 or filas > 6) or (columnas < 2 or columnas > 6) or (filas == 6 and columnas == 6):
                    print("Error: Board dimensions must be between 2x2 and 6x5 (also valid 5x6). Please try again.")
                elif (filas * columnas) % 2 != 0:
                    print("Error: Board size must have an even number of positions. Please try again.")
                else:
                    return filas, columnas
            except ValueError:
                print("Error: Enter a valid number.")

    '''
    createHiddenBoard() method. creates the board displayed to the player with no emojis.
    '''
    def crear_tablero_oculto(self):
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append("_")
            self.tablero_oculto.append(fila)
        return self.tablero_oculto

    '''
    createPairsBoard() method. creates the board the user has to guess.
    '''
    def crear_tablero_parejas(self):
        emojis = [
            "😀", "😁", "😂", "🤣", "😃", "😄", "😅", "😆", "😉", "😊", "😋", "😎", "😍",
            "😘", "😗", "😙", "😚", "🤗", "🤔", "😐", "😑", "😶", "😏", "🙄", "😮", "😯",
            "😴", "🤤", "😪", "😵", "🤐", "🥴", "🤢", "🤧", "🥳", "🤠", "😇"
        ]
        parejas = (random.sample(emojis, (self.filas * self.columnas) // 2)) * 2
        random.shuffle(parejas)
        pos = 0
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append(parejas[pos])
                pos += 1
            self.tablero_parejas.append(fila)
        
        return self.tablero_parejas

    '''
    showHidden() method. prints the board used to play.
    '''
    def mostrarOculto(self):
        for i in self.tablero_oculto:
            print(" ".join(i))

    '''
    showEmojis() method. prints the solved board.
    '''
    def mostrarEmojis(self):
        for i in self.tablero_parejas:
            print(" ".join(i))

    '''
    show() method. prints the board with the new discovered card.
    '''
    def mostrar(self, f, c):
        self.tablero_oculto[f][c] = self.tablero_parejas[f][c]
    
    '''
    hidden() method. hides a card if the player fails trying to guess a pair.
    '''
    def ocultar(self, f, c):
        self.tablero_oculto[f][c] = "_"
    
    '''
    check() method. receives two rows and two columns. compares if the two cards given are the same.
    '''
    def comprobar(self, f1, c1, f2, c2):
        if (self.tablero_parejas[f1][c1] == self.tablero_parejas[f2][c2]):
            return True
        else:
            return False
        
    '''
    isShown() method. receives row and column. checks if the card is already flipped.
    '''
    def estaMostrado(self, f, c):
        if self.tablero_oculto[f][c] != "_":
            return True
        else:
            return False

    '''
    getMaxPoints() method. returns the max score. MAY MOVE THIS METHOD TO CLASS PLAYER.
    '''
    def getMaxPoints(self):
        return self.max_points
