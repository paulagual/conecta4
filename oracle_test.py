import pytest

from oracle import *
from square_board import SquareBoard
from player import Player
from settings import *

def test_base_oracle():
    board = SquareBoard.fromList([[None, None, None, None],
                                  ['x','o','x','o'],
                                  ['o','o','x','x'],
                                  ['o', None, None, None]])
    expected = [ColumnRecommendation(0, ColumnClassification.MAYBE),
                ColumnRecommendation(1, ColumnClassification.FULL),
                ColumnRecommendation(2, ColumnClassification.FULL),
                ColumnRecommendation(3, ColumnClassification.MAYBE)]

    rappel = BaseOracle()

    assert len(rappel.get_recommendation(board, None)) == len(expected)
    assert rappel.get_recommendation(board, None) == expected

def test_equality():
    cr = ColumnRecommendation(2, ColumnClassification.MAYBE)

    #identicos
    assert cr == cr 
    
    #equivalente
    assert cr == ColumnRecommendation(2, ColumnClassification.MAYBE)
    assert cr == ColumnRecommendation(1, ColumnClassification.MAYBE)

    # no equivalentes
    assert cr != ColumnRecommendation(2, ColumnClassification.FULL) 
    assert cr != ColumnRecommendation(3, ColumnClassification.FULL) 


if BOARD_LENGTH == 4 and VICTORY_STRIKE == 3:
    def test_is_winning_move():
        winner = Player('Xavier', 'x')
        loser = Player('Otoo', 'o')

        empty = SquareBoard()
        
        board = SquareBoard.fromList([[None, None, None, None],
                                    ['x','o', 'x', 'o'],
                                    ['o','x', None, None],
                                    ['x', 'x', None, None]])

        oracle = SmartOracle()

        # comprobar sobre tablero vacío
        for i in range(0,BOARD_LENGTH):
            assert oracle._is_winning_move(empty, i, winner) == False
            assert oracle._is_winning_move(empty, i, loser) == False

        for i in range(0,BOARD_LENGTH):
            assert oracle._is_winning_move(board, i, loser) == False
        

        assert oracle._is_winning_move(board, 3, winner) 

    def test_is_losing_move():
        loser = Player('Xavier', 'x')
        winner = Player('Otoo', 'o')
        loser.opponent = winner
        winner.opponent = loser

        empty = SquareBoard()
        
        board = SquareBoard.fromList([[None, None, None, None],
                                    ['o','o', 'x', 'o'],
                                    ['x','o', None, None],
                                    ['o', 'x', None, None]])

        oracle = SmartOracle()

        #comprobar sobre tablero vacío
        for i in range(0,BOARD_LENGTH):
            assert oracle._is_losing_move(empty, i, loser) == False
            assert oracle._is_losing_move(empty, i, winner) == False

        #comrpobar sobre board
        for i in range(0,BOARD_LENGTH):
            assert oracle._is_losing_move(board, i, winner) == False

        assert oracle._is_losing_move(board, 1, loser)     

    def test_no_good_options():

        x = Player('X', char = 'x')
        o = Player('O', char = 'o')
        o.opponent = x
        x.opponent = o

        oracle = SmartOracle()

        maybe = SquareBoard.fromBoardRawCode('....|o...|....|....')
        bad_and_full = SquareBoard.fromBoardRawCode('x...|oo..|o...|xoxo')
        all_bad = SquareBoard.fromBoardRawCode('x...|oo..|o...|....')

        assert oracle.no_good_options(maybe, x) == False
        assert oracle.no_good_options(bad_and_full, x) 
        assert oracle.no_good_options(all_bad, x)
