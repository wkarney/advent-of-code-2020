from day1 import expense_report_pairs
import pytest

example_input = [1721, 979, 366, 299, 675, 1456]
duplicate_example = [5, 2, 0, 1010]  # Cannot use the same expense twice.


def test_pt1_example():
    """Test day 1 part 1 example"""
    assert expense_report_pairs(example_input, 2020, 2) == 514579


def test_pt2_example():
    """Test day 1 part 2 example"""
    assert expense_report_pairs(example_input, 2020, 3) == 241861950


def test_duplicate_expense_exception():
    """Test day 1 edge case to ensure digits aren't double-counted"""
    with pytest.raises(Exception):
        expense_report_pairs(duplicate_example, 2020, 2)
