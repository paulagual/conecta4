
from beautifultable import BeautifulTable

from enum import Enum, auto

from match import Match
from player import Player, HumanPlayer, ReportingPlayer
from square_board import SquareBoard
from list_utils import reverse_matrix
from oracle import SmartOracle, BaseOracle, MemoizingOracle, LearningOracle
from settings import BOARD_LENGTH

class RoundType(Enum):
    COMPUTER_VS_COMPUTER = auto()
    COMPUTER_VS_HUMAN = auto()

class DifficultyLevel(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()

class Game():    

    def __init__(self, round_type = RoundType.COMPUTER_VS_COMPUTER, match = Match(ReportingPlayer('Chip'), ReportingPlayer('Chop'))):
        self.round_type = round_type
        self.match = match
        self.board = SquareBoard()

    def start(self):
        #imprimo el nombre del juego
        self.print_logo()

        #configuro la partida
        self._configure_by_user()

        #arranco el game loop
        self._start_game_loop()


    def print_logo(self):
        logo = """


 ██████  ██████  ███    ██ ███████  ██████ ████████  █████  
██      ██    ██ ████   ██ ██      ██         ██    ██   ██ 
██      ██    ██ ██ ██  ██ █████   ██         ██    ███████ 
██      ██    ██ ██  ██ ██ ██      ██         ██    ██   ██ 
 ██████  ██████  ██   ████ ███████  ██████    ██    ██   ██ 
                                                            
                                                                                          
"""
        print(logo)

    def _start_game_loop(self):
        while True:
            #obtengo el jugador que va a jugar
            current_player = self.match.next_player

            #le hago jugar
            current_player.play(self.board)

            #muestro su jugada
            self.display_move(current_player)
            
            #imprimo el tablero
            self.display_board()

            #si el juego ha terminado == si hay una victoria
            if self._is_game_over() :
                #muestro el resultado final
                self.display_result()
                break

    def display_move(self, player):
        """ 
        Imprimir el movimiento del jugador
        """
        print(f"El jugador {player.name} ha jugado con el char {player.char} en la columna {player.last_move.position}")

    def display_board(self):
        """
        Imprimir el tablero, usando beautifultable
        """
        #pasar el board a una matriz
        matrix = self.board.as_matrix()

        #invertir la matriz
        matrix = reverse_matrix(matrix)

        #create a beautiful table
        bt = BeautifulTable()

        for col in matrix:
            bt.columns.append(col)
        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]    

        #imprimirla
        print(bt)


    def display_result(self):
        """ 
        Imprimir el resultado de la partida, ya sea el ganador o que hay empate
        """
        winner = self.match.get_winner(self.board)
        if winner != None:
            print(f"El ganador es {winner.name} que juega con la ficha {winner.char}")
        else:
            print(f"/n Hay un empate")

    def _is_game_over(self):
        """ 
        Verifica si el juego ha terminado: hay una victoria o un empate (el tablero lleno)
        """
        winner = self.match.get_winner(self.board) #un vencedor 'x' o 'o' o si no lo hay None

        return (winner != None) or (self.board.is_full())

    def _configure_by_user(self):
        """ 
        Con la info del tipo de partida que quiere el jugador, configurar el game y el match
        """
        #determinar tipo de partida
        self.round_type = self._get_round_type()

        #determinar el nivel de dificultad
        if self.round_type == RoundType.COMPUTER_VS_HUMAN:
            self._dificulty_level = self._get_difficulty_level()

        #crear la partida
        self.match = self._make_match()

    def _get_round_type(self):
        """
        Pedir al usuario el tipo de partida que quiere jugar
        """
        print("""
        Elige un tipo de partida:

        1.- Ordenador vs. Ordenador
        2.- Humano vs. Ordenador
        
        """)
        response = ""

        while response != "1" and response != "2":
            response= input("Por favor, elije 1 o 2: ").strip()
        
        if response == "1":
            return RoundType.COMPUTER_VS_COMPUTER       
        else:
            return RoundType.COMPUTER_VS_HUMAN

    def _get_difficulty_level(self):
        """
        Pedir al usuario el tipo de dificultad que quiere jugar 
        """
        print("""
        Elige el nivel de dificultad de tu oponente:

        1.- Muy fácil
        2.- Medio
        3.- Dificil
        
        """)
        response = ""

        while response != "1" and response != "2" and response != "3":
            response= input("Por favor, elije 1, 2 o 3: ").strip()
    
        if response == "1":
            return DifficultyLevel.EASY 
        elif response == "2":
            return DifficultyLevel.MEDIUM 
        else:
            return DifficultyLevel.HARD 

    def _make_match(self):
        """
        El player 1 siempre será robot, el jugador 2 depende de la elección del usuario.        
        """
        _levels = {DifficultyLevel.EASY: BaseOracle(),
                   DifficultyLevel.MEDIUM: SmartOracle(),
                   DifficultyLevel.HARD: LearningOracle()}

        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            #ambos jugadores roboticos
            player1 = ReportingPlayer('T-X', oracle=LearningOracle())
            player2 = ReportingPlayer('T-O', oracle=LearningOracle())
        else:
            #jugador 1 robotico, jugador 2 humano
            player1 = ReportingPlayer('T-X', oracle=_levels[self._dificulty_level])
            player2 = HumanPlayer(name = input("¿Cuál es tu nombre? "))

        return Match(player1, player2)