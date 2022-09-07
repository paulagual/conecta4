from oracle import *
from square_board import *
from linear_board import *

class Player():
    
    def __init__(self, name, player, oracle = BaseOracle()):
        self.name = name
        self.player = player
        self._oracle = oracle

    def play(self, board):
        """
        Elige la mejor columna de entre las que te ofrece el oráculo
        """
        #obtener recomendaciones
        recommendations = self._oracle.get_recommedation(board, self)

        #seleccionar la mejor recomendacion
        best = self._choose(recommendations)

        #jugar en la columna recomendada
        board.add(self.player, best.index)
        
        return board

    def _choose(self, recommedations):
        #quitamos las columnas no válidas
        posible = list(filter(lambda x: x.classification != ColumnClassification.FULL, recommedations))

        #elegimos la primera
        return posible[0]

        