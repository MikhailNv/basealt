import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test3 import CheckingGID

cr = CheckingGID()

def test_access():
    assert (cr.access() == True)

def test_ccreate_file():
    assert (cr.create_file() == True)

def test_setting_first_new_rights():
    assert (cr.setting_new_rights('rx') == True)

def test_operations_on_files():
    assert (cr.operations_on_files() == True)

def test_setting_second_new_rights():
    assert (cr.setting_new_rights('w') == True)

def test_check_rights_for_ivk2():
    assert (cr.check_rights_for_ivk2() == True)