from square_board import SquareBoard
from enum import Enum, auto

class ColumnClassification(Enum):
        
        FULL = auto()
        MAYBE = auto()

class ColumnRecommendation():
    
    def __init__(self, index, classification):
        self.index = index
        self.classification = classification

    # dunders

    def __eq__(self, other):
        #si son de clases distintas, son distintos
        if not isinstance(other, self.__class__):
            return False
        #si son de la misma clase, compara sus elementos   
        else:
            return (self.index, self.classification) == (other.index, other.classification)
    
    def __hash__(self) -> int:
        return hash((self.index, self.classification))

class BaseOracle():

    def __init__(self):
        pass
    
    def get_recommedation(self, board, char):
        """
        Devuelve una lista de ColumnRecommedations
        """
        recommedation = []
        for i in range(len(board)):
            recommedation.append(self.get_column_recommendation(board, i, char))

        return recommedation

    def get_column_recommendation(self, board, index, char):
        """
        Devuelve la clasificacion para una columna entre FULL y MAYE y devuelve una ColumnRecommendation
        """
        classification = ColumnClassification.MAYBE

        if board._columns[index].is_full():
            classification = ColumnClassification.FULL

        return ColumnRecommendation(index, classification)