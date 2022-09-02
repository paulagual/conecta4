from settings import BOARD_LENGTH, VICTORY_STRIKE

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
        Comprueba si un jugador concreto ha ganado 
        """
        strike = 0
        i = 0
        while strike < VICTORY_STRIKE and i < BOARD_LENGTH:
            if self._column[i] == player:
                strike +=1
            else:
                strike = 0
            i += 1

        return strike >= VICTORY_STRIKE
        
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