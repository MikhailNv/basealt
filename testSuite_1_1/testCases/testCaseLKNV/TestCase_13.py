import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test13 import Sgid

cr = Sgid()

def test_first_adding_atribut():
    assert (cr.adding_atribut('u:ivk3:rwx') == True)

def test_first_ivk3_commands():
    assert (cr.ivk3_commands() == [True, True, True])

def test_second_adding_atribut():
    assert (cr.adding_atribut('m::r') == True)

def test_second_ivk3_commands():
    assert (cr.ivk3_commands() == [False, True, False])