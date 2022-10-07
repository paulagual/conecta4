from beautifultable import BeautifulTable

from move import Move
from oracle import *
from square_board import *
from linear_board import *
from list_utils import all_same
import random


class Player():
    
    def __init__(self, name, char = None, opponent = None, oracle = BaseOracle()):
        self.name = name
        self.char = char
        self._oracle = oracle
        self.opponent = opponent
        self.last_moves = []

    @property
    def opponent(self):
        return self._opponent
    
    @opponent.setter
    def opponent(self, other):
        self._opponent = other
        if other != None:
            other._opponent = self

    def play(self, board):
        """
        Elige la mejor columna de entre las que te ofrece el oráculo
        """
        # Preguntar al Oráculo
        (best, recommendations) = self._ask_oracle(board)

        # Jugar la mejor jugada
        self.play_on(board, best.index, recommendations)

    def _ask_oracle(self, board):
        """
        Pregunta al oráculo y devuelve la mejor opción y las recomendaciones
        """
        #obtener recomendaciones
        recommendations = self._oracle.get_recommendation(board, self)
       
        #seleccionar la mejor recomendacion
        best = self._choose(recommendations)

        return (best, recommendations)

    def on_win(self):
        pass

    def on_lose(self):
        pass

    def play_on(self, board, position, recommendations):
        """
        Juega en la posición indicada
        """
        #jugar en la columna 
        board.add(self.char, position)

        #guardo la última jugada siempre al principio de la lista
        self.last_moves.insert(0, Move(position, board.as_code(), recommendations, self))

    def _choose(self, recommendations):
        #quitamos las columnas no válidas
        posible = list(filter(lambda x: x.classification != ColumnClassification.FULL, recommendations))

        #ordenar por el valor de clasificación, primero las WIN y luego las MAYBE
        valid = sorted(posible, key=lambda x: x.classification.value, reverse = True)

        #si, todas son iguales, elegimos al azar entre las posibles
        if all_same(valid):
            return random.choice(valid)
            #si no lo son, cojo la primera que será la mejor
        else:
            return valid[0]

class HumanPlayer(Player):

    def __init__(self, name, player = None):
        super().__init__(name, player)

    def _ask_oracle(self, board):
        """
        Le pido al humamo (es el oráculo del human player)
        """
        while True:
            #pedir columna al humano
            col = input('Elige una columna en la que jugar (o h para pedir ayuda): ')

            #si pide ayuda darsela
            if col.lower() == "h":
                opponent = self.opponent

                #create a beautiful table
                bt_rec = BeautifulTable()

                #añadir las recomendaciones
                for i in range(BOARD_LENGTH):
                    recomendation = opponent._oracle._get_column_recommendation(board, i, opponent.opponent)
                    bt_rec.columns.append([recomendation])
                
                #poner el header
                bt_rec.columns.header = [str(i) for i in range(BOARD_LENGTH)]    

                #imprimirla
                print(bt_rec)


            #verificar que es una respuesta válida
            if _is_int(col) and _is_within_column_range(board, int(col)) and _is_non_full_column(board, int(col)):
            #si no lo es, jugamos la jugada
                pos = int(col)
                return (ColumnRecommendation(pos, None), None)


class ReportingPlayer(Player):

    def on_lose(self):
        """
        Le pide al oráculo que revise sus recomendaciones
        """
        self._oracle.backtrack(self.last_moves)











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