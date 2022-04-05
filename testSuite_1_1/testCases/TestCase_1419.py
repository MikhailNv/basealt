import unittest
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks"))
from test4 import CheckingRules1419


class TestCase_1419(unittest.TestCase):

    thing = None

    @classmethod
    def setUpClass(cls):
        print("\n")
        pwd = input("[sudo] password: ")
        print("\n")
        cls.thing = CheckingRules1419(pwd)  # the `thing` is only instantiated once

    def setUp(self) -> None:
        self.cr = TestCase_1419.thing

    def test_add(self):
        self.assertEqual(self.cr.check_add_users_and_groups(), True)

    def test_change_password_testuser(self):
        self.assertEqual(self.cr.check_change_password_testuser('q1w2e3r4'), True)

    def test_prohibition_of_change(self):
        self.assertEqual(self.cr.prohibition_of_change(), True)

    def test_check_change_passwd_with_root(self):
        self.assertEqual(self.cr.check_change_passwd_with_root(), True)

    def test_delete_data(self):
        self.assertEqual(self.cr.delete_data(), True)
