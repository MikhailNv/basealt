import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test1 import CheckingUID

cr = CheckingUID()

def test_add_ivk1():
    assert (cr.add_ivk1() == True)

def test_check_input_for_ivk1():
    assert (cr.check_input_for_ivk1() == True)

def test_change_chmod():
    assert (cr.change_chmod() == True)

def test_read_file_with_ivk1():
    assert (cr.read_file_with_ivk1() == True)