import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test05 import CatalogGID

cr = CatalogGID()

def test_create_file_and_dir():
    assert (cr.create_file_and_dir() == True)

def test_change_rights():
    assert (cr.change_rights() == True)

def test_users_rights_first_chech():
    assert (cr.check_users_rights('ivk1', 'file1') == True)

def test_users_rights_second_chech():
    try:
        cr.check_users_rights('ivk2', 'file2')
    except Exception as e:
        assert (e.args[0] == 'Touch file error (ivk2)')

def test_new_owner_rights():
    assert (cr.new_owner_rights() == True)

def test_users_rights_third_chech():
    try:
        cr.check_users_rights('ivk1', 'file3')
    except Exception as e:
        assert (e.args[0] == 'Touch file error (ivk1)')