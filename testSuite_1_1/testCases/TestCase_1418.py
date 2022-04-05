import unittest
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks"))
from test3 import CheckingRules1418

class TestCase_1418(unittest.TestCase):

    def setUp(self):
        self.cr = CheckingRules1418()

    def test_view_list(self):
        self.assertEqual(self.cr.view_list_of_directories(), True)

    def test_file_creation(self):
        self.assertEqual(self.cr.check_created_files(), True)

    def test_file_copy(self):
        self.assertEqual(self.cr.check_copy_file(), True)

    def test_recursion_copy(self):
        self.assertEqual(self.cr.check_recursion_copy(), True)

    def test_move_file(self):
        self.assertEqual(self.cr.check_move_file(), True)

    def test_remove_file(self):
        self.assertEqual(self.cr.check_remove_file(), True)

    def test_remove_catalog(self):
        self.assertEqual(self.cr.check_remove_catalog(), True)

    def test_search_validation(self):
        self.assertEqual(self.cr.search_validation(), True)