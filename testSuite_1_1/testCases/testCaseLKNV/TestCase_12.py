import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test12 import Suid

cr = Suid()

def test_adding_atribut():
    assert (cr.adding_atribut() == True)

def test_first_change_ivk1_passwd():
    assert (cr.change_ivk1_passwd() == True)

def test_first_rule_updates():
    assert (cr.rule_updates('u-s') == True)

def test_second_change_ivk1_passwd():
    assert (cr.change_ivk1_passwd() == True)

def test_second_rule_updates():
    assert (cr.rule_updates('g+s') == True)

def test_third_change_ivk1_passwd():
    assert (cr.change_ivk1_passwd() == True)

def test_third_rule_updates():
    assert (cr.rule_updates('a-s') == True)

def test_fourth_change_ivk1_passwd():
    assert (cr.change_ivk1_passwd() == True)