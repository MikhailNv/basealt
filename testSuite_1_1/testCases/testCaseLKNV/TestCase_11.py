import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testLKNV"))
from test11 import RootRestriction

cr = RootRestriction()

def test_start_settings():
    assert (cr.start_settings() == True)

def test_view_root_permissions():
    assert (cr.view_root_permissions() == True)

def test_restriction_of_root_rights():
    assert (cr.restriction_of_root_rights() == True)

def test_restoration_of_rights():
    assert (cr.restoration_of_rights() == True)