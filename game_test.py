import pytest

from game import Game
from square_board import SquareBoard
from settings import *


def test_creation():
    g = Game()
    
    assert g != None

if BOARD_LENGTH == 4 and VICTORY_STRIKE == 3 :
    def test_game_over():
        x_victory = Game()
        x_victory.board = SquareBoard.fromList([['x', 'o', None, None,],
                                        ['o', 'x', None, None,],
                                        ['x', 'o', 'x', 'o',],
                                        ['x', 'x', None, None,],
                                        ['x', 'o', None, None,]])    

        o_victory = Game()
        o_victory.board = SquareBoard.fromList([['x', 'o', None, None,],
                                        ['o', 'x', None, None,],
                                        ['x', 'o', 'o', 'o',],
                                        ['x', 'x', None, None,],
                                        ['x', 'o', None, None,]])    
        full = Game()
        full.board = SquareBoard.fromList([['x', 'o', 'x', 'o',],
                                    ['o', 'x', 'o', 'x',],
                                    ['x', 'x', 'o', 'x',],
                                    ['o', 'o', 'x', 'o',],
                                    ['x', 'x', 'o', 'o',]])  
        
        not_over = Game()
        not_over.board = SquareBoard.fromList([['x', 'o', None, None,],
                                        ['o', 'x', None, None,],
                                        ['x', 'o', None, None,],
                                        ['x', 'x', None, None,],
                                        [None, None, None, None,]])  
        

        assert x_victory._has_winner_or_tie()
        assert o_victory._has_winner_or_tie() 
        assert full._has_winner_or_tie() 
        assert not_over._has_winner_or_tie() == False

    