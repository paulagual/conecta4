import pytest

from list_utils import *
from oracle import ColumnRecommendation, ColumnClassification

def test_find_one():
    needle = 1
    none = [0, 0, 5, 's']
    begining = [1, None, 9, 3, 5, 6]
    end = ['x', '0', 1]
    several = [0, 0, 3, 1, 4, 1, 1, 3]

    assert find_one(none, needle) == False
    assert find_one(begining,needle) == True
    assert find_one(end,needle) == True
    assert find_one(several,needle) #No hace falta poner == True

def test_find_n():    
    assert find_n([2, 0, 0, 5, 8], 2, -1) == False
    assert find_n([1, 2, 3 , 4, 5], 42, 2) == False
    assert find_n([1, 2, 3 , 4, 5], 1, 2) == False
    assert find_n([2, 0, 2, 5, 8, 9], 2, 2) == True
    assert find_n([2, 0, 0, 4, 9, 4, 5, 8, 4, 5, 7, 4, 6], 4, 2) #No hace falta poner == True
    assert find_n([1, 0, 0, 5, 8], 'x', 0) 

def test_find_streak():
    assert find_streak([2, 0, 0, 5, 8], 4, -1) == False
    assert find_streak([1, 2, 3, 4, 5], 42, 2) == False
    assert find_streak([1, 2, 3 , 4, 5], 4, 1) == True
    assert find_streak([1, 2, 3 , 2, 5], 2, 2) == False
    assert find_streak([5, 5, 5, 0, 2, 5, 8, 9], 5, 3) 
    assert find_streak([0, 2, 5, 8, 9, 5, 5, 5], 5, 3) 
    assert find_streak([0, 2, 5, 5, 5, 6, 7, 5], 5, 3) 
    assert find_streak([0, 2, 5, 8, 9, 5, 5, 5], 5, 4) == False 

def test_first_elements():
    original = [[0,7,3], [4,0,1]]

    assert first_elements(original) == [0,4]


def test_nth_elements():
    original = [[0,7,3], [4,0,1], [4,6,7]]

    assert nth_elements(original, 1) == [7,0,6]

def test_transpose():
    original = [[0,7,3], [4,0,1], [4,6,7]]
    original2 = [[0,7,3], [4,0,1]]

    assert transpose(original) == [[0,4,4], [7,0,6], [3,1,7]]
    assert transpose(original2) == [[0,4], [7,0],[3,1]]
    assert transpose(transpose(original2)) == original2

def test_zero_distance_displace():
    l1 = [1,2,3,4,5,6]
    l2 = [1]
    l3 = [[4,5], ['x','o','c']]

    assert displace([],0) == []
    assert displace(l1,0) == l1 
    assert displace(l2,0) == l2 
    assert displace(l3,0) == l3 

def test_positive_distance_displace():
    l1 = [1,2,3,4,5,6]
    l2 = [1]
    l3 = [[4,5], ['x','o','c']]
    l4 = [9,6,5]

    assert displace([],2) == []
    assert displace(l1,2) == [None, None, 1,2,3,4]
    assert displace(l2,3, '-') == ['-'] 
    assert displace(l3,1,'#') == ['#',[4,5]] 
    assert displace(l4,3,0) == [0,0,0] 

def test_negative_distance_displace():
    l1 = [1,2,3,4,5,6]
    l2 = [1]
    l3 = [[4,5], ['x','o','c']]
    l4 = [9,6,5]

    assert displace([],-2) == []
    assert displace(l1,-2) == [3,4,5,6, None, None]
    assert displace(l2,-3, '-') == ['-'] 
    assert displace(l3,-1,'#') == [['x','o','c'],'#'] 
    assert displace(l4,3,0) == [0,0,0] 

def test_reverse_list():
    assert reverse_list([]) == []
    assert reverse_list([1,2,3,4,5,6]) == [6,5,4,3,2,1]

def test_reverse_matrix():
    assert reverse_matrix([]) == []
    assert reverse_matrix([[0,1,2,3],[0,1,2,3]]) == [[3,2,1,0],[3,2,1,0]]

def test_all_same():

    ls = [1,'w', [1,2], {'x':1, 'o':2}, 5]



    assert all_same([])
    assert all_same([None, None]) 
    assert all_same([1, 1, 1]) 
    assert all_same([1, 2, 1]) == False
    assert all_same([2, 2, 1]) == False
    assert all_same([1, 2, 2]) == False
    assert all_same(['x', 'x', 'x']) 
    assert all_same([ls, ls, ls]) 
    assert all_same([ls, ls, 'ls']) == False
    assert all_same([[],[],[]])
    assert all_same([ColumnRecommendation(1, ColumnClassification.MAYBE), 
                    ColumnRecommendation(0, ColumnClassification.MAYBE)])

    assert all_same([ColumnRecommendation(0, ColumnClassification.WIN), 
                    ColumnRecommendation(0, ColumnClassification.MAYBE)]) == False
