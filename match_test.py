import pytest

from player import Player, HumanPlayer
from match import Match


xavier = None
otto = None

def setup():
    """
    Se ejecuta previo a cada test de este listado de tests
    para inicializar el contenido de las variables globales
    """
    global xavier #tiene que inicializar ñas variables globales, para todos los test
    xavier = HumanPlayer('Xavier')

    global otto 
    otto = Player('Otto')

def teardown():
    """
    Se ejecuta posterior a cada test de este listado de tests 
    para borrar el contenido de las variables globales
    """
    global xavier #tiene que inicializar ñas variables globales, para todos los test
    xavier = None

    global otto 
    otto = None


def test_different_players_have_different_chars():
    t = Match(xavier, otto)

    assert xavier.player != otto.player


def test_no_player_with_no_char():
    t = Match(xavier, otto)

    assert xavier.player != None
    assert otto.player != None

def test_no_player_with_no_char():
    t = Match(otto, xavier)
    p1 = t.next_player
    p2 = t.next_player
    
    assert p1 != p2

def test_players_are_opponents():
    t = Match(otto, xavier)
    p1 = t.next_player
    p2 = t.next_player
    
    assert p1.opponent == p2    
    assert p2.opponent == p1        