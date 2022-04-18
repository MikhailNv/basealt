import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test8 import ClassACL

cr = ClassACL()

def test_getfacl():
    assert (cr.getfacl() == True)

def test_first_check_rights():
    assert (cr.check_rights() == True)

def test_add_rights():
    assert (cr.add_rights() == True)

def test_second_check_rights():
    assert (cr.check_rights() == True)