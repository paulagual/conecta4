from oracle import *
from square_board import *
from linear_board import *

class Player():
    
    def __init__(self, name, player = None, opponent = None, oracle = BaseOracle()):
        self.name = name
        self.player = player
        self._oracle = oracle
        self.opponent = opponent

    @property
    def opponent(self):
        return self._opponent
    
    @opponent.setter
    def opponent(self, other):
        if other != None:
            self._opponent = other
            other._opponent = self

    def play(self, board):
        """
        Elige la mejor columna de entre las que te ofrece el oráculo
        """
        # Preguntar al Oráculo
        (best, recommendations) = self._ask_oracle(board)

        # Jugar la mejor jugada
        self.play_on(board, best.index)

    def _ask_oracle(self, board):
        """
        Pregunta al oráculo y devuelve la mejor opción y las recomendaciones
        """
        #obtener recomendaciones
        recommendations = self._oracle.get_recommedation(board, self)
       
        #seleccionar la mejor recomendacion
        best = self._choose(recommendations)

        return (best, recommendations)

    def play_on(self, board, index):
        """
        Juega en la posición indicada
        """
        #jugar en la columna 
        board.add(self.player, index)

        return board

    def _choose(self, recommedations):
        #quitamos las columnas no válidas
        posible = list(filter(lambda x: x.classification != ColumnClassification.FULL, recommedations))

        #elegimos la primera
        return posible[0]

class HumanPlayer(Player):

    def __init__(self, name, player = None):
        super().__init__(name, player)

    def _ask_oracle(self, board):
        """
        Le pido al humamo (es el oráculo del human player)
        """
        while True:
            #pedir columna al humano
            col = input('Elige una columna en la que jugar (or h for help): ')
    
            #verificar que es una respuesta válida
            if _is_int(col) and _is_within_column_range(board, int(col)) and _is_non_full_column(board, int(col)):
            #si no lo es, jugamos la jugada
                pos = int(col)
                return (ColumnRecommendation(pos, None), None)

#funciones que validan la entrada del humano

def _is_within_column_range(board, column):
    return column >= 0 and column < len(board)

def _is_non_full_column(board, column):
    return not board._columns[column].is_full()

def _is_int(n):
    try:
        num = int(n)
        return True
    except:
        return False