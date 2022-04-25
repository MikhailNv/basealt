import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test15 import Immutable

cr = Immutable()

def test_adding_atribut():
    assert (cr.adding_atribut('a', 'b') == True)

def test_first_ivk1_commands():
    assert (cr.ivk1_commands(1, 'b') == True)

def test_removing_atribut():
    assert (cr.removing_atribut('a', 'b') == True)

def test_second_ivk1_commands():
    assert (cr.ivk1_commands(2, 'b') == True)