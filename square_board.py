from settings import BOARD_LENGTH, VICTORY_STRIKE
from linear_board import LinearBoard
from list_utils import *

class SquareBoard():
    """
    Representa un tablero cuadrado compusto por n linear boards
    """
    @classmethod
    def fromList(cls, list_of_lists):
        """
        Transforma una lista de listas en una list de linearBoards
        """
        board = cls()
        board._columns = list(map(lambda element: LinearBoard().fromList(element), list_of_lists))
        return board

    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_LENGTH)] 
    
    def as_matrix(self):
        """
        Devuelve una representación de self en formato de matriz, lista de listas
        """
        return list(map(lambda x: x._column, self._columns))

    def is_full(self):
        """ 
        Comprueba si el tablero está lleno.
        True si todos los linearBoards están llenos
        """  
        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result
        

    def is_victory(self, player):
        """
        Detecta los 4 tipos de victoria: vertical, horizontal, diagonal ascendente y diagola descendente
        """
        return self._any_vertical_victory(player) or self._any_horizontal_victory(player) or self._any_rising_victory(player) or self._any_sinking_victory(player)

    
    def _any_vertical_victory(self, player):
        """
        Comprueba si hay una victoria vertical en el tablero
        """
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(player)
        return result

    def _any_horizontal_victory(self, player):
        """
        Comprueba si hay una victoria horizontal en el tablero
        """
        #transpongo la representacion del board
        transposed = transpose(self.as_matrix())

        #creo un tablero virtual para no modificar el real
        tmp = SquareBoard.fromList(transposed)

        #busco una victoria vertical
        return tmp._any_vertical_victory(player)

    def _any_rising_victory(self, player):
        """
        Comprueba si hay una victoria diagonal ascendente en el tablero
        """
        m = reverse_matrix(self.as_matrix())
        tmp = SquareBoard.fromList(m)
        return tmp._any_sinking_victory(player)

    def _any_sinking_victory(self, player):
        """
        Comprueba si hay una victoria diagonal descendente en el tablero
        """
        m = self.as_matrix()
        d = displace_matrix(m)
        tmp = SquareBoard.fromList(d)
        return tmp._any_horizontal_victory(player)

    # dunders

    def __repr__(self):
        return f'{self.__class__}:{self._columns}'   

    def __len__(self):
        return len(self._columns)