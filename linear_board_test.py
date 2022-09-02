import pytest
from linear_board import *
from settings import BOARD_LENGTH, VICTORY_STRIKE

def test_empty_board():
    empty = linearBoard()
    assert empty != None
    assert empty.is_full() == False
    assert empty.is_victory('x') == False

def test_add():
    b = linearBoard()
    for i in range(BOARD_LENGTH):
        b.add('x')
    assert b.is_full() == True

def test_add_to_full():
    full = linearBoard()

    for i in range(BOARD_LENGTH):
        full.add('x')
    
    full.add('x')

    assert full.is_full() == True
    


def test_victory():
    b = linearBoard()
    for i in range(VICTORY_STRIKE):
        b.add('x')

    assert b.is_victory('o') == False
    assert b.is_victory('x') == True

def test_tie():
    b = linearBoard()

    b.add('o')
    b.add('x')   
    b.add('x')   
    b.add('o')  

    assert b.is_tie('x','o')

