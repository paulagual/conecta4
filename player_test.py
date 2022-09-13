import pytest 

from oracle import *
from linear_board import *
from square_board import *
from player import Player, _is_within_column_range, _is_int, _is_non_full_column

#esto ha cambiado y ya no se da, ya no jugamos en la primera opción disponible

# def test_play():    
#     """
#     Test para comprobar que juega en la primera columna disponible
#     """

#     before = SquareBoard.fromList([['x', 'o', None, None,],
#                               ['o', 'x', None, None,],
#                               ['x', 'o', 'x', 'o',],
#                               ['x', 'x', 'x', 'o',],
#                               ['x', 'o', None, None,]])

#     after = SquareBoard.fromList([['x', 'o', 'x', None,],
#                               ['o', 'x', None, None,],
#                               ['x', 'o', 'x', 'o',],
#                               ['x', 'x', 'x', 'o',],
#                               ['x', 'o', None, None,]])
    
#     player = Player('Chip', 'x', oracle=BaseOracle())

#     player.play(before)

#     assert before == after

def test_valid_column():
    board = SquareBoard.fromList([['x', None, None, None,],
                              ['x', 'o', 'x', 'o',],
                              ['x', 'o', 'x', 'x',],
                              ['o', None, None, None,]])
    
    assert _is_within_column_range(board, 0)
    assert _is_within_column_range(board, 1)
    assert _is_within_column_range(board, 2)
    assert _is_within_column_range(board, 3)
    assert _is_within_column_range(board, 5) == False
    assert _is_within_column_range(board, -10) == False
    assert _is_within_column_range(board, 10) == False

def test_non_full_column():
    board = SquareBoard.fromList([['x', None, None, None,],
                              ['x', 'o', 'x', 'o',],
                              ['x', 'o', 'x', 'x',],
                              ['o', None, None, None,]])

    assert _is_non_full_column(board, 0)
    assert _is_non_full_column(board, 1) == False
    assert _is_non_full_column(board, 2) == False
    assert _is_non_full_column(board, 3)

def test_in_int():
    assert _is_int('42')
    assert _is_int('0')
    assert _is_int('-32')
    assert _is_int('    32    ')
    assert _is_int('hola') == False        
    assert _is_int('') == False        
    assert _is_int('3.14') == False            