import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test07 import ClassUID

cr = ClassUID()

def test_change_rights():
    assert (cr.change_rights() == True)

def test_first_check_rights():
    assert (cr.check_rights() == [False, True])

def test_add_the_right_to_write():
    assert (cr.add_the_right_to_write() == True)

def test_second_check_rights():
    assert (cr.check_rights() == [True, True])