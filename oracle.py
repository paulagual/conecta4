from square_board import SquareBoard
from copy import deepcopy
from enum import Enum, auto
from settings import BOARD_LENGTH

class ColumnClassification(Enum):
        FULL    =  -1 #imposible de jugar
        LOSE   =   1 #derrota casi asegurada
        MAYBE   =  10 #puedes jugar, pero es indeseable
        WIN     = 100 #la mejor opción, gano seguro

class ColumnRecommendation():
    
    def __init__(self, index, classification):
        self.index = index
        self.classification = classification

    # dunders

    def __eq__(self, other):
        #si son de clases distintas, son distintos
        if not isinstance(other, self.__class__):
            return False
        #si son de la misma clase, compara sólo la clasificación
        else:
            return self.classification == other.classification
    
    def __hash__(self) -> int:
        return hash(self.classification)

class BaseOracle():

    def __init__(self):
        pass
    
    def get_recommedation(self, board, player):
        """
        Devuelve una lista de ColumnRecommedations
        """
        recommedation = []
        for i in range(len(board)):
            recommedation.append(self._get_column_recommendation(board, i, player))

        return recommedation

    def _get_column_recommendation(self, board, index, player):
        """
        Devuelve la clasificacion para una columna entre FULL y MAYE y devuelve una ColumnRecommendation
        """
        classification = ColumnClassification.MAYBE

        if board._columns[index].is_full():
            classification = ColumnClassification.FULL

        return ColumnRecommendation(index, classification)

class SmartOracle(BaseOracle):
    
    def _get_column_recommendation(self, board, index, player):
        """
        Afina la clasificacion de super para encontrar columnas WIN
        """
        #obtenemos la recomendacion generica
        recommendation = super()._get_column_recommendation(board, index, player)

        #si es MAYBE buscamos una mejor
        if recommendation.classification == ColumnClassification.MAYBE:
            #busca si hay una jugada ganadora para recomendarla
            if self._is_winning_move(board, index, player):
                recommendation.classification = ColumnClassificatio.WIN
            #si no, busca si hay una jugada perdedora para evitarla
            elif self._is_losing_move(board, index, player):
                recommendation.classification = ColumnClassificatio.LOSE

        return recommendation

    def _is_losing_move(self, board, index, player):
        """
        Detecta columnas donde un jugador juega en una posición, su oponente tendrá una jugada gandora
        """
        
        # hacemos el movimiento en el board temporal
        tmp = self._play_on_tmp_board(board, index, player)
       
        will_loose = False

        #para todos los posibles movimientos del oponente burcamos si hay una victoria
        for i in range(0,BOARD_LENGTH):
            if self._is_winning_move(tmp, i, player.opponent):
                will_loose = True
                break
        return will_loose

    def _is_winning_move(self, board, index, player):
        """
        Detecta columnas donde hay una vitoria segura 
        """
        # hacemos el movimiento en el board temporal
        tmp = self._play_on_tmp_board(board, index, player)
        
        #comprobamos si hay una victoria en el tmp board
        return tmp.is_victory(player)

    def _play_on_tmp_board(self, board, index, char):
        """ 
        Juega en un board temporal
        """
        #creamos copia del board
        tmp_board = deepcopy(board)

        #jugamos en el board temporal
        tmp_board.add(char, index)

        #devuelve el tmp board con el movimiento añadido
        return tmp_board



       