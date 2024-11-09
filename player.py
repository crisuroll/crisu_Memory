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
        self.carta = None

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
        if self.nivel and self.nivel >= 2:
            self.memory[(fila, columna)] = carta
            if self.nivel == 2 and len(self.memory) > 2:
                self.memory = dict(list(self.memory.items())[-2:])
        print("Estado de memory:", self.memory)

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
    
    # REVISAR ESTE METODO.
    def elegir_con_memoria(self, tablero):
        """
        Elige cartas basándose en la memoria de cartas previas.
        Si hay una carta seleccionada (self.carta), intenta encontrar su pareja.
        Si no, busca parejas en memoria o elige una nueva carta aleatoria.
        """
        # Caso 1: Si tenemos una carta seleccionada previamente
        if self.carta is not None:
            fila1, col1 = self.carta
            carta_valor = self.memory.get((fila1, col1))
        
            # Buscar pareja para la carta seleccionada
            for (f, c), valor in self.memory.items():
                if (f, c) != (fila1, col1) and valor == carta_valor and not tablero.estaMostrado(f, c):
                    self.carta = None  # Resetear la selección
                    return f, c
        
            # Si no encontramos pareja, resetear y elegir nueva carta
            self.carta = None
    
        # Caso 2: Buscar parejas conocidas en memoria
        for (f1, c1), valor1 in self.memory.items():
            if tablero.estaMostrado(f1, c1):
                continue
            
            for (f2, c2), valor2 in self.memory.items():
                if (f1, c1) != (f2, c2) and valor1 == valor2 and not tablero.estaMostrado(f2, c2):
                    self.carta = (f1, c1)  # Guardar primera carta
                    return f1, c1
    
        # Caso 3: Si no hay parejas conocidas, elegir carta aleatoria
        f, c = self.elegir_aleatorio(tablero)
        self.carta = (f, c)  # Guardar la carta elegida
        return f, c

    '''
    chooseExpert() method. the CPU memory remembers all cards and tries to make pairs strategically.
    '''
    def elegir_con_estrategia(self, tablero):
        # Inicializar memoria completa si está vacía
        if not self.memory:
            for f in range(tablero.filas):
                for c in range(tablero.columnas):
                    self.memory[(f, c)] = tablero.tablero_parejas[f][c]
    
        return self.elegir_con_memoria(tablero)
