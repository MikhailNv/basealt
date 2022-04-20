import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test06 import CatalogACL

cr = CatalogACL()

def test_change_dir_rights():
    assert (cr.change_dir_rights() == True)

def test_first_additional_rule():
    assert (cr.additional_rule('wx') == True)

def test_users_rights_first_check():
    assert (cr.check_users_rights('ivk1', 'fb') == [False, False, False])

def test_users_rights_second_check():
    assert (cr.check_users_rights('ivk3', 'fb') == [False, True, True])

def test_second_additional_rule():
    assert (cr.additional_rule('r') == True)

def test_users_rights_third_check():
    assert (cr.check_users_rights('ivk3', 'fb') == [True, False, False])

def test_change_first_rights():
    assert (cr.change_first_rights() == True)

def test_users_rights_fourth_check():
    assert (cr.check_users_rights('ivk1', 'fb') == [False, False, False])

def test_users_rights_fifth_check():
    assert (cr.check_users_rights('ivk2', 'fb1') == [True, False, True])

def test_change_second_rights():
    assert (cr.change_second_rights() == True)

def test_users_rights_sixth_check():
    assert (cr.check_users_rights('ivk2', 'fb') == [False, False, False])

def test_users_rights_seventh_check():
    assert (cr.check_users_rights('ivk3', 'fb') == [True, False, False])

def test_change_third_rights():
    assert (cr.change_third_rights() == True)

def test_users_rights_eght_check():
    assert (cr.check_users_rights('ivk3', 'fb') == [False, True, True])