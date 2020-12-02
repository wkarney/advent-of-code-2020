from day2 import count_officially_valid_passwords
from day2 import count_valid_passwords


def test_pt1_ex1():
    """Test day 2 part 1 examples"""
    assert count_valid_passwords(["1-3 a: abcde"]) == 1
    assert count_valid_passwords(["1-3 b: cdefg"]) == 0
    assert count_valid_passwords(["2-9 c: ccccccccc"]) == 1


def test_pt2_example():
    """Test day 2 part 2 examples"""
    assert count_officially_valid_passwords(["1-3 a: abcde"]) == 1
    assert count_officially_valid_passwords(["1-3 b: cdefg"]) == 0
    assert count_officially_valid_passwords(["2-9 c: ccccccccc"]) == 0
