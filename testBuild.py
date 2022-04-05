import unittest
import subprocess
from testSuite_1_1.testCases.TestCase_1415 import TestCase_1415
from testSuite_1_1.testCases.TestCase_1416 import TestCase_1416
from testSuite_1_1.testCases.TestCase_1417 import TestCase_1417
from testSuite_1_1.testCases.TestCase_1418 import TestCase_1418
from testSuite_1_1.testCases.TestCase_1419 import TestCase_1419

def check_packages():
    update = subprocess.run('apt-get -y update'.split(), stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                         shell=False, encoding='utf-8')
    if update.returncode != 0:
        return update.stderr
    else:
         packages = ['gimp', 'vlc', 'vim-console', 'xorg-xvfb', 'pip']
         f = open("cat.txt", 'w')
         for i in range(len(packages)):
             print(f"Installing package {packages[i]}")
             install = subprocess.run(f'apt-get install -y --force-yes {packages[i]}'.split(), stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE,
                                      encoding='utf-8')
             if install.returncode != 0:
                 return install.stderr
         cmd = ['rm', 'cat.txt']
         subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, encoding='utf-8')
         return "Все пакеты успешно установлены"


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCase_1415))
    suite.addTest(unittest.makeSuite(TestCase_1416))
    suite.addTest(unittest.makeSuite(TestCase_1417))
    suite.addTest(unittest.makeSuite(TestCase_1418))
    suite.addTest(unittest.makeSuite(TestCase_1419))
    return suite

if __name__ == '__main__':
    print("Проверка пакетов...")
    #print(check_packages())
    runner = unittest.TextTestRunner()
    runner.run(suite())
