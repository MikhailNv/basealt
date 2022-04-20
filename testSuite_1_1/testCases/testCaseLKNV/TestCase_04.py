import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test04 import CheckingSecondGID

cr = CheckingSecondGID()

def test_add_ivk1():
    assert (cr.add_ivk3() == True)

def test_first_viewing_rights():
    assert (cr.viewing_rights('rwx') == True)

def test_first_check_rights():
    assert (cr.check_rights('ivk3') == '/dtest/file1: line 1: 123: command not found')

def test_second_check_rights():
    assert (cr.check_rights('ivk2') == '-bash: /dtest/file1: Permission denied')

def test_second_viewing_rights():
    assert (cr.viewing_rights('rx') == True)

def test_third_check_rights():
    assert (cr.check_rights('ivk3') == '-bash: /dtest/file1: ')