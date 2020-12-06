from day6 import count_sum_of_unique_yes_answers
from day6 import count_sum_of_universal_yes_answers

example_data = ["abc", "a\n\nb\nc", "ab\nac", "a\na\na\na", "b"]


def test_example_day6_pt1():
    """Test day 6 pt 1 example"""
    assert count_sum_of_unique_yes_answers(example_data) == 11


def test_example_day6_pt2():
    """Test day 6 pt 2 example"""
    assert count_sum_of_universal_yes_answers(example_data) == 6
