from calculator import operations as op
import pytest

def test_add():
    assert op.add(2, 3) == 5

def test_subtract():
    assert op.subtract(5, 3) == 2

def test_multiply():
    assert op.multiply(4, 3) == 12

def test_divide():
    assert op.divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        op.divide(1, 0)

def test_exponent():
    assert op.exponent(2, 3) == 8

def test_modulus():
    assert op.modulus(10, 3) == 1
    with pytest.raises(ZeroDivisionError):
        op.modulus(1, 0)
