import pytest

from string_utils import *

def test_collapse_list():
    assert collapse_list([]) == ''
    assert collapse_list(['o','x','x','o']) == 'oxxo'
    assert collapse_list(['o','x', None, None]) == 'ox..'

def test_collapse_matrix():
    assert collapse_matrix([]) == ''
    assert collapse_matrix([['o','x','x'],
                            ['o',None,None],
                            ['x','x',None]]) == 'oxx|o..|xx.'

def test_explode_string():
    assert explode_string('Han') == ['H','a','n']
    assert explode_string('') == []

def test_explode_list_of_strings():
    assert explode_list_of_strings(['Han','Solo']) == [['H','a','n'],['S','o','l','o']]
    assert explode_list_of_strings(['','','']) == [[],[],[]]
    assert explode_list_of_strings([]) == []

def test_replace_all_in_list():
    assert replace_all_in_list([None, 3, '3', 43, None, 4], None, '#') == ['#', 3, '3', 43, '#', 4]
    assert replace_all_in_list([None, 3, '3', 43, None, 4], 'e', 42) == [None, 3, '3', 43, None, 4]
    assert replace_all_in_list([], 34, 45) == []


def test_replace_all_in_matrix():
    assert replace_all_in_matrix([], None, 7) == []
    assert replace_all_in_matrix([[],[],[]], None, 7) == [[],[],[]]
    assert replace_all_in_matrix([[0,0],[0,1],[1,0],[1,1]],1,None) == [[0,0],[0,None],[None,0],[None,None]]
    assert replace_all_in_matrix([[0,0],[0,1],[1,0],[1,1]],2,33) == [[0,0],[0,1],[1,0],[1,1]]
