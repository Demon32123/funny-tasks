import pytest
from solution import strict

@strict
def sum_three_int(a: int, b: int, c: int) -> int:
    return a + b + c

@strict
def sum_two_int(a: int, b: int) -> int:
    return a + b

@strict
def sum_three_float(a: float, b: float, c: float) -> float:
    return a + b + c

@strict
def sum_two_float(a: float, b: float) -> float:
    return a + b

@strict
def string_check(a: str) -> str:
    return a

@strict
def bool_check(a: bool) -> bool:
    return a

def test_sum_two_int():
    with pytest.raises(TypeError):
        sum_two_int(1, 10.3)
    assert sum_two_int(1, 1) == 2

def test_sum_two_float():
    with pytest.raises(TypeError):
        sum_two_float(2.5, 1)
    assert sum_two_float(1.1, 2.3) == 3.4

def test_sum_three_float():
    with pytest.raises(TypeError):
        sum_three_float(1, 10.0, 2)
    assert sum_three_float(1.1, 1.5, 2.3) == 4.9

def test_sum_three_int():
    with pytest.raises(TypeError):
        sum_three_int(1.2, 5, 4)
    assert sum_three_int(1, 1, 1) == 3

def test_string():
    with pytest.raises(TypeError):
        string_check(True)
    assert string_check("True") == "True"

def test_bool():
    with pytest.raises(TypeError):
        bool_check("hi, world")
    assert bool_check(False) == False


