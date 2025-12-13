import sys
from pathlib import Path
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from Calculatorapp import add, subtract, multiplication, division, log10, square, sqrt, sin, cos, percentage

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_subtract():
    assert subtract(10, 6) == 4

def test_subtract2():
    assert subtract(10, 6) != 5

def test_multiplication():
    assert multiplication(2, 8) == 16

def test_multiplication2():
    assert multiplication(2, 8) != 19

def test_division():
    assert division(6, 3) == 2

def test_division2():
    assert division(6, 3) != 3

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(6, 0)

def test_log10():
    with pytest.raises(ValueError):
        log10(-1)

def test_log10_2():
    assert log10(10) == 1

def test_log10_3():
    assert log10(10) != 5

def test_square():
    assert square(5) == 25

def test_square2():
    assert square(5) != 30

def test_sqrt():
    assert sqrt(36) == 6

def test_sqrt2():
    assert sqrt(36) != 10

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-36)

def test_sin():
    assert abs(sin(90) - 1.0) < 1e-6

def test_cos():
    assert abs(cos(0) - 1.0) < 1e-6

def test_percentage():
    assert percentage(50) == 0.5

def test_percentage2():
    assert percentage(50) != 0.4
