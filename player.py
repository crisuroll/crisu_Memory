###################################################################
from random import randint
###################################################################

class Player:
    '''
    constructor. attributes name and score.
    '''
    def __init__(self, name, nivel=0):
        self.name = name
        self.score = 0
        self.nivel = nivel  # Nivel de dificultad, 0 para un jugador humano
        self.memory = {} if nivel > 0 else None  # Memoria solo si es CPU

    # PREGUNTAR A HECTOR POR QUE NO ME FUNCIONA @property NI @setter

    '''
    getters
    ''' 
    def getName(self):
        return self.name
    
    def getScore(self):
        return self.score
    
    '''
    setters
    '''
    def setName(self,name):
        self.name = name

    def setScore(self):
        self.score += 2



    '''
    addCard() method. adds a card to the CPU memory from medium level and above.
    '''
    def recordar_carta(self, fila, columna, carta):
        ''' Almacena una carta en la memoria en función del nivel de dificultad '''
        if self.nivel and self.nivel >= 2:
            self.memory[(fila, columna)] = carta
            if self.nivel == 2 and len(self.memory) > 2:
                self.memory = dict(list(self.memory.items())[-2:])

    '''
    chooseCards() method. the CPU chooses the cards based on its difficulty level.
    '''
    def elegir_cartas(self, tablero):
        match self.nivel:
            case 1:
                return self.elegir_aleatorio(tablero)
            case 2:
                return self.elegir_con_memoria(tablero, limit=2)
            case 3:
                return self.elegir_con_memoria(tablero)
            case 4:
                return self.elegir_con_estrategia(tablero)

    '''
    chooseRandom() method. chooses two random cards that are not revealed. easy level.
    '''
    def elegir_aleatorio(self, tablero):
        descubiertas = set()
        while True:
            fila1, col1 = randint(0, tablero.filas - 1), randint(0, tablero.columnas - 1)
            if not tablero.estaMostrado(fila1, col1):
                descubiertas.add((fila1, col1))
                break

        while True:
            fila2, col2 = randint(0, tablero.filas - 1), randint(0, tablero.columnas - 1)
            if not tablero.estaMostrado(fila2, col2) and (fila2, col2) not in descubiertas:
                break
        return (fila1, col1), (fila2, col2)


    # REVISAR DIFICULTADES. NO TERMINADAS.

    '''
    chooseWithMemory() method. chooses two cards. if a card is in the CPU memory, chooses it and tries to make a pair. 
    if it's medium level, the CPU only remembers the last two cards. if it's hard level, remembers all cards.
    '''
    def elegir_con_memoria(self, tablero, limit=None):
        for (f1, c1), card1 in self.memory.items():
            for (f2, c2), card2 in self.memory.items():
                if (f1, c1) != (f2, c2) and card1 == card2:
                    return (f1, c1), (f2, c2)
        return self.elegir_aleatorio(tablero)

    '''
    chooseExpert() method. the CPU memory remembers all cards and tries to make pairs strategically.
    '''
    def elegir_con_estrategia(self, tablero):
        return

