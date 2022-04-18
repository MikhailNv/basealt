import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test9 import ClassGID

cr = ClassGID()

def test_delete_rights():
    assert (cr.delete_rights() == True)

def test_check_rights_ivk1():
    assert (cr.check_rights('ivk1') == True)

def test_check_rights_ivk2():
    assert (cr.check_rights('ivk2') == True)