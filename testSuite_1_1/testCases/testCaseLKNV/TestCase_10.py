import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test10 import ClassGID

cr = ClassGID()

def test_first_rights_change():
    assert (cr.first_rights_change() == True)

def test_check_rights_ivk2():
    assert (cr.check_rights('ivk2') == True)

def test_first_check_rights_ivk3():
    assert (cr.check_rights('ivk3') == True)

def test_second_rights_change():
    assert (cr.second_rights_change() == True)

def test_second_check_rights_ivk3():
    assert (cr.check_rights('ivk3') == True)