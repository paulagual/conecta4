from settings import BOARD_LENGTH, VICTORY_STRIKE
from list_utils import find_streak

class linearBoard():
    """
    Clase que representa un tablero de una sola columna
    x un jugador
    0 otro jugador
    None un espacio vacío
    """
    def __init__(self):
        """ 
        Una lista de None 
        """
        self._column = [None for i in range(BOARD_LENGTH)]

    def is_full(self):
        """ 
        Comprueba si la columna está llena 
        """
        return self._column[-1] != None
    
    def is_victory(self, player):
        """ 
        Comprueba si un jugador concreto tiene más de VICTORY_STRIKES seguidas 
        """
        return find_streak(self._column, player, VICTORY_STRIKE)
        
    def add(self, move):
        """
        Juega en la primera posición disponible
        """
        if not self.is_full():
            i = self._column.index(None)
            self._column[i] = move

    def is_tie(self, player1, player2):
        """ 
        Comprueba si ha habido un empate, es decir no hay victoria ni de 'x' ni de 'o'
        """
        
        return (self.is_victory(player1) == False) and (self.is_victory(player2) == False) 

    def __str__(self):
        return "Linear Board"

    def __repr__(self):
        return self.__str__()