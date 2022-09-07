import pytest 

from oracle import *
from linear_board import *
from square_board import *
from player import *

def test_play():    
    """
    Test para comprobar que juega en la primera columna disponible
    """

    before = SquareBoard.fromList([['x', 'o', None, None,],
                              ['o', 'x', None, None,],
                              ['x', 'o', 'x', 'o',],
                              ['x', 'x', 'x', 'o',],
                              ['x', 'o', None, None,]])

    after = SquareBoard.fromList([['x', 'o', 'x', None,],
                              ['o', 'x', None, None,],
                              ['x', 'o', 'x', 'o',],
                              ['x', 'x', 'x', 'o',],
                              ['x', 'o', None, None,]])
    
    player = Player('Chip', 'x', oracle=BaseOracle())

    player.play(before)

    assert before == after