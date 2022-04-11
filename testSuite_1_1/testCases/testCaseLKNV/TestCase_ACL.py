import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test2 import CheckingACL

cr = CheckingACL()

def test_add_ivk1():
    assert (cr.add_ivk2() == True)

def test_add_first_rights():
    assert (cr.add_rights('-m user:ivk2:rw') == True)

def test_check_first_rights_ivk2():
    assert (cr.check_rights_ivk2('before') == True)

def test_add_second_rights():
    assert (cr.add_rights('-x u:ivk2') == True)

def test_check_second_rights_ivk2():
    assert (cr.check_rights_ivk2('after') == True)