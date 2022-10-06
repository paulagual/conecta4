from settings import BOARD_LENGTH, VICTORY_STRIKE
from linear_board import *
from list_utils import *
from string_utils import *

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
    
    @classmethod
    def fromBoardCode(cls, board_code):
        return cls.fromBoardRawCode(board_code.raw_code)

    @classmethod
    def fromBoardRawCode(cls, board_raw_code):
        #convertir la cadena del codigo en una lista de cadenas
        list_of_strings = board_raw_code.split('|')

        #transformar cada cadena en una lista de caracteres
        matrix = explode_list_of_strings(list_of_strings)

        #cambianos todos los . por None
        matrix = replace_all_in_matrix(matrix,'.',None)

        #transformamos la lista en SquareBoard
        return cls.fromList(matrix)

    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_LENGTH)] 
    
    def as_matrix(self):
        """
        Devuelve una representación de self en formato de matriz, lista de listas
        """
        return list(map(lambda x: x._column, self._columns))

    def as_code(self):
        """
        Convierte un SquareBoard a code
        """
        return BoardCode(self)

    def add(self, char, column):
        """
        Juega una ficha en una columna
        """
        self._columns[column].add(char)

    def is_full(self):
        """ 
        Comprueba si el tablero está lleno.
        True si todos los linearBoards están llenos
        """  
        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result
        

    def is_victory(self, char):
        """
        Detecta los 4 tipos de victoria: vertical, horizontal, diagonal ascendente y diagola descendente
        """
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)

    
    def _any_vertical_victory(self, char):
        """
        Comprueba si hay una victoria vertical en el tablero
        """
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(char)
        return result

    def _any_horizontal_victory(self, char):
        """
        Comprueba si hay una victoria horizontal en el tablero
        """
        #transpongo la representacion del board
        transposed = transpose(self.as_matrix())

        #creo un tablero virtual para no modificar el real
        tmp = SquareBoard.fromList(transposed)

        #busco una victoria vertical
        return tmp._any_vertical_victory(char)

    def _any_rising_victory(self, char):
        """
        Comprueba si hay una victoria diagonal ascendente en el tablero
        """
        m = reverse_matrix(self.as_matrix())
        tmp = SquareBoard.fromList(m)
        return tmp._any_sinking_victory(char)

    def _any_sinking_victory(self, char):
        """
        Comprueba si hay una victoria diagonal descendente en el tablero
        """
        m = self.as_matrix()
        d = displace_matrix(m)
        tmp = SquareBoard.fromList(d)
        return tmp._any_horizontal_victory(char)
    


    # dunders

    def __repr__(self):
        return f'{self.__class__}:{self._columns}'   

    def __len__(self):
        return len(self._columns)

    def __eq__(self, other):
         #si son de clases distintas, son distintos
        if not isinstance(other, self.__class__):
            return False
        #si son de la misma clase, compara sus elementos   
        else:
            return self._columns == other._columns

    def __hash__(self):
        return hash(self._columns)

class BoardCode:
    
    def __init__(self,board):
        self._raw_code = collapse_matrix(board.as_matrix())

    @property
    def raw_code(self):
        return self._raw_code

    # dunders
    def __eq__(self, other):
         #si son de clases distintas, son distintos
        if not isinstance(other, self.__class__):
            return False
        #si son de la misma clase, compara sus elementos   
        else:
            return self.raw_code == other.raw_code

    def __hash__(self):
        return hash(self.raw_code)

    def __repr__(self):
        return f'{self.__class__}:{self.raw_code}'   