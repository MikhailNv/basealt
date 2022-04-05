import unittest
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks"))
from test_gui_program import GuiProgram

class TestCase_1415(unittest.TestCase):

    def setUp(self):
        self.cr = GuiProgram()

    def test_firefox(self):
        self.assertEqual(self.cr.check_running_app('firefox'), True)

    def test_gimp(self):
        self.assertEqual(self.cr.check_running_app('gimp'), True)

    def test_vlc(self):
        self.assertEqual(self.cr.check_running_app('vlc'), True)

    def test_vim(self):
        self.assertEqual(self.cr.check_running_app('vim'), True)
