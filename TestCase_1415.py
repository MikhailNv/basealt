import pytest
import os, sys
import subprocess
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks/testARMH"))
from test_gui_program import GuiProgram

cr = GuiProgram()

log = {'expected_results': 'none'}
log_html = 'none'


# Функция переназначения глобальных переменных
def set_global_var(expected_results='none', html='none'):
    global log, log_html
    log = {'expected_results': expected_results}
    log_html = html


# Фикстура, которая автоматически, перед каждым тестом будет сбрасывать значения глобальных переменных
@pytest.fixture(scope="function", autouse=True)
def default_global_var():
    set_global_var()

def test_firefox():
    '''Test 1'''
    res = cr.check_running_app('firefox')
    if res == True:
        set_global_var(expected_results='Vse horosho')
    else:
        set_global_var(expected_results=res)
    assert (res == True)

def test_gimp():
    '''Test 2'''
    res = cr.check_running_app('gimp')
    if res == True:
        set_global_var(expected_results='Vse horosho')
    else:
        set_global_var(expected_results=res)
    assert (res == True)

def test_vlc():
    '''Test 3'''
    res = cr.check_running_app('vlc')
    if res == True:
        set_global_var(expected_results='Vse horosho')
    else:
        set_global_var(expected_results=res)
    assert (res == True)

def test_vim():
    '''Test 4'''
    res = cr.check_running_app('vim')
    if res == True:
        set_global_var(expected_results='Vse horosho')
    else:
        set_global_var(expected_results=res)
    assert (res == True)
