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
        self.memory = dict() if nivel > 0 else None  # Memoria solo si es CPU

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
        print("Estado de memory antes de agregar:", self.memory)
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
        while True:
            f, c = randint(0, tablero.filas - 1), randint(0, tablero.columnas - 1)
            if not tablero.estaMostrado(f, c):
                return f, c


    # REVISAR DIFICULTADES. NO TERMINADAS.

    '''
    chooseWithMemory() method. chooses two cards. if a card is in the CPU memory, chooses it and tries to make a pair. 
    if it's medium level, the CPU only remembers the last two cards. if it's hard level, remembers all cards.
    '''
    def elegir_con_memoria(self, tablero):
        for (f1, c1), card1 in self.memory.items():
            for (f2, c2), card2 in self.memory.items():
                if (f1, c1) != (f2, c2) and card1 == card2 and not tablero.estaMostrado(f1, c1) and not tablero.estaMostrado(f2, c2):
                    return f1, c1

        return self.elegir_aleatorio(tablero)

    '''
    chooseExpert() method. the CPU memory remembers all cards and tries to make pairs strategically.
    '''
    def elegir_con_estrategia(self, tablero):
        pareja = self.elegir_con_memoria(tablero)
        if pareja:
            return pareja

        for f in range(tablero.filas):
            for c in range(tablero.columnas):
                if not tablero.estaMostrado(f, c) and (f, c) not in self.memory:
                    return f, c

        return self.elegir_aleatorio(tablero)

