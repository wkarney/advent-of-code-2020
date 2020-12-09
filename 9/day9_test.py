from day9 import find_first_invalid_value
from day9 import find_pt2


with open("9/ex-input.txt") as f:
    ex_data = [int(line) for line in f]


def test_example_day9_pt1():
    """Test day 9 pt 1 example"""
    assert find_first_invalid_value(ex_data, 5) == 127


def test_example_day9_pt2():
    """Test day 9 pt 2 example"""
    assert find_pt2(ex_data, 127) == 62
