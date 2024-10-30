###################################################################
import random
###################################################################

class Board:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero_oculto = []
        self.tablero_parejas = []
        self.max_points = (self.filas * self.columnas) // 2
        self.crear_tablero_oculto()
        self.crear_tablero_parejas()

    @staticmethod
    def pedir_dimensiones():
        while True:
            try:
                filas = int(input("Dime el número de filas: "))
                columnas = int(input("Dime el número de columnas: "))
                if (filas < 2 or filas > 6) or (columnas < 2 or columnas > 6) or (filas == 6 and columnas == 6):
                    print("Error: Dimensiones deben estar entre 2x2 y 6x5. Vuelve a intentarlo.")
                elif (filas * columnas) % 2 != 0:
                    print("Error: Número total de posiciones debe ser par. Vuelve a intentarlo.")
                else:
                    return filas, columnas
            except ValueError:
                print("Error: Introduce un número válido.")

    def crear_tablero_oculto(self):
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append("_")
            self.tablero_oculto.append(fila)
        return self.tablero_oculto

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

    def mostrarOculto(self):
        for i in self.tablero_oculto:
            print(" ".join(i))

    def mostrar(self, f, c):
        self.tablero_oculto[f][c] = self.tablero_parejas[f][c]
    
    def ocultar(self, f, c):
        self.tablero_oculto[f][c] = "_"
    
    def comprobar(self, f1, c1, f2, c2):
        if (self.tablero_parejas[f1][c1] == self.tablero_parejas[f2][c2]):
            return True
        else:
            return False
        
    def estaMostrado(self, f, c):
        if self.tablero_oculto[f][c] != "_":
            return True
        else:
            return False

    def getMaxPoints(self):
        return self.max_points
