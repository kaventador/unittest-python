import calculator

def test_positive():
    assert calculator.sqr(2)==4
    assert calculator.sqr(3)==9
    assert calculator.sqr(4)==16

def test_negative():
    assert calculator.sqr(-2) == 4
    assert calculator.sqr(-3) == 9
    assert calculator.sqr(-4) == 16

def test_zero():
    assert calculator.sqr(0) == 0
