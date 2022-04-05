import unittest
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks"))
from test1 import CheckingRules1416

class TestCase_1416(unittest.TestCase):
    def setUp(self):
        self.cr = CheckingRules1416()

    # Проверка на определение интерфейса
    def test_ip_link(self):
        self.assertEqual(self.cr.check_working_interface()[0], "Интерфейс определен")

    # Проверка статистики прерываний на запущенном интерфейсе
    def test_cat(self):
        cat = self.cr.check_interrupts(self.cr.check_working_interface()[1])
        self.assertEqual(cat, True)

    def test_down(self):
        self.assertEqual(self.cr.check_interface_is_down(), True)

    def test_is_up(self):
        self.assertEqual(self.cr.check_interface_is_up(), True)

    def test_interrupts(self):
        self.assertEqual(type(self.cr.get_interrupts()), int)
