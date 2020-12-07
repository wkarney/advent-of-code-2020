import re

from day4 import count_valid_passport_pt2
from day4 import REQUIRED_FIELDS


with open("4/ex_valids_pt2.txt") as f:
    valid_data = f.read()
valid_data_input = re.split(r"(?:\r?\n){2,}", valid_data.strip())

with open("4/ex_invalids_pt2.txt") as f:
    invalid_data = f.read()
invalid_data_input = re.split(r"(?:\r?\n){2,}", invalid_data.strip())


def test_count_valid_passport_pt2():
    """Test day 4 pt 2 examples"""
    assert count_valid_passport_pt2(valid_data_input, REQUIRED_FIELDS) == 4
    assert count_valid_passport_pt2(invalid_data_input, REQUIRED_FIELDS) == 0
