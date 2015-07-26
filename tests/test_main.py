from mock import patch
from cuts.main import lst, main
from nose.tools import raises


def original_text():
    return "This is a test.\nThis is only a test."

def sample_out1():
    '''cuts -f 1,-1 -d " "'''
    return "This\ttest.\nThis\ttest."

def test_lst():
    assert lst("1,2,3,4,5") == ['1','2','3','4','5']

@raises(SystemExit)
def test_main_no_args():
    assert main([])

@raises(SystemExit)
def test_main_too_many_options():
    assert main(['-b','-1','-f','-1'])

@raises(SystemExit)
def test_zero_position_1():
    assert(main(['-f','0']))

@raises(SystemExit)
def test_zero_position_2():
    assert(main(['-f','1,0']))

@raises(SystemExit)
def test_zero_position_3():
    assert(main(['-f','1,0:']))

@raises(SystemExit)
def test_zero_position_4():
    assert(main(['-f','1,0:5']))

@raises(SystemExit)
def test_zero_position_5():
    assert(main(['-f','1,:0']))

@raises(SystemExit)
def test_zero_position_6():
    assert(main(['-f','1,-4:0']))
