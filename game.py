
from enum import Enum, auto

from match import Match
from player import Player, HumanPlayer
from square_board import SquareBoard

class RoundType(Enum):
    COMPUTER_VS_COMPUTER = auto()
    COMPUTER_VS_HUMAN = auto()

class DifficultyLevel(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()

class Game():    

    def __init__(self, round_type = RoundType.COMPUTER_VS_COMPUTER, match = Match(Player('Chip'), Player('Chop'))):
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
        
    def _start_game_loop():
        pass 

    def _configure_by_user(self):
        #determinar tipo de partida
        self.round_type = self._get_round_type()

        #crear la partida
        self.match = self._make_match()

    def _get_round_type(self):
        """
        Pedir al usuario el tipo de partida que quiere jugar y el nivel de dificultad.
        """
        print("""
        Elige un tipo de partida:

        1.- Ordenador vs. Ordenador
        2.- Humano vs. Ordenador
        
        """)
        response = ""

        while response != "1" and response != "2":
            response= input("Por favor, elije 1 o 2: ")
        
        if response == "1":
            return RoundType.COMPUTER_VS_COMPUTER       
        else:
            return RoundType.COMPUTER_VS_HUMAN

    def _make_match(self):
        """
        El player 1 siempre será robot, el jugador 2 depende de la elección del usuario.        
        """
        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            #ambos jugadores roboticos
            player1 = Player('T-X')
            player2 = Player('T-O')
        else:
            #jugador 1 robotico, jugador 2 humano
            player1 = Player('T-X')
            player2 = HumanPlayer(name = input("¿Cuál es tu nomrbe? "))

        return Match(player1, player2)