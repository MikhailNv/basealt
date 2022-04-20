import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test14 import StickyBit

cr = StickyBit()

def test_adding_atribut():
    assert (cr.adding_and_removing_atribut('1777') == True)

def test_first_ivk3_commands():
    assert (cr.ivk3_commands(1) == True)

def test_removing_atribut():
    assert (cr.adding_and_removing_atribut('-t') == True)

def test_second_ivk3_commands():
    assert (cr.ivk3_commands(2) == True)