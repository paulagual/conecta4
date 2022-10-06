import pytest

from square_board import * 

def test_empty_board():
    b = SquareBoard()

    assert b.is_full() == False
    assert b.is_victory('o') == False
    assert b.is_victory('x') == False

def test_vertical_victory():
    vertical = SquareBoard.fromList([['o','x','x','x',],
                                    [None, None, None, None,],
                                    [None, None, None, None,],
                                    [None, None, None, None,],
                                    [None, None, None, None,]])
    assert vertical.is_victory('x')
    assert vertical.is_victory('o') == False

def test_horizontal_victory():
    horizontal = SquareBoard.fromList([['x', None, None, None,],
                                    ['x', None, None, None,],
                                    ['o', 'o', None, None,],
                                    ['x', 'o', None, None,],
                                    ['x', 'o', None, None,]])
    assert horizontal.is_victory('o')
    assert horizontal.is_victory('x') == False

def test_sinking_victory():
    sinking = SquareBoard.fromList([['x', 'o','x', 'o',],
                                    ['x', 'x', 'o', None,],
                                    ['o', 'o', None, None,],
                                    ['o', 'x', None, None,],
                                    ['x', None, None, None,]])
    assert sinking.is_victory('o')
    assert sinking.is_victory('x') == False

def test_rising_victory():
    rising = SquareBoard.fromList([['x', 'o', None, None,],
                                    ['o', 'x', None, None,],
                                    ['x', 'o', 'x', 'o',],
                                    ['x', 'x', None, 'o',],
                                    ['x', 'o', None, None,]])
    assert rising.is_victory('x')
    assert rising.is_victory('o') == False

def test_eq():
    a = SquareBoard.fromList([['x', 'o', None, None,],
                              ['o', 'x', None, None,],
                              ['x', 'o', 'x', 'o',],
                              ['x', 'x', 'x', 'o',],
                              ['x', 'o', None, None,]])

    b = SquareBoard.fromList([['x', 'o', None, None,],
                              ['o', 'x', None, None,],
                              ['x', 'o', 'x', 'o',],
                              ['x', 'x', 'x', 'o',],
                              ['x', 'o', None, None,]])

    assert a == b

def test_board_code():
    board = SquareBoard.fromList([['x', 'o', None, None,],
                              ['o', 'x', None, None,],
                              ['x', 'o', 'x', 'o',],
                              ['x', 'x', 'x', 'o',],
                              ['x', 'o', None, None,]])

    code = board.as_code()
    
    clone_board = SquareBoard.fromBoardCode(code)

    assert clone_board == board
    assert clone_board.as_code() == code
    assert clone_board.as_code().raw_code == code.raw_code