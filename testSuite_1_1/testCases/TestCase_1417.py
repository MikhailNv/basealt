import unittest
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks"))
from test2 import CheckingRules1417

class TestCase_1417(unittest.TestCase):
    def setUp(self):
        self.cr = CheckingRules1417()

    def test_create_file(self):
        self.assertEqual(self.cr.create_file(), "Файл создан")

    def test_buffer(self):
        check_buffer_100 = self.cr.check_buffer('100K')
        check_buffer_1 = self.cr.check_buffer('1G')
        self.assertEqual(check_buffer_100[0], "Создание буфера выполнено корректно")
        self.assertEqual(check_buffer_1[0], "Создание буфера выполнено корректно")
        self.assertTrue(check_buffer_100[1] != check_buffer_1[1])

    def test_delete_file(self):
        self.assertEqual(self.cr.delete_access_file(), 0)
