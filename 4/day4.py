#!/usr/bin/env python

"""
Advent of Code 2020, day 4
Will Karnasiewicz
"""

import re

REQUIRED_FIELDS_1 = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def split_on_empty_lines(s):
    """Split string at empty line"""
    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())


# Part 1


def count_valid_passport_pt1(input_txt, required_fields):
    """Docstring TK"""
    passport_fields = []
    for groupings in input_txt:
        field_list = [item.split(":")[0] for item in re.split(r"\s", groupings)]
        passport_fields.append(field_list)

    valids = 0
    for individual in passport_fields:
        status = 1
        for item in required_fields:
            if item not in individual:
                status = 0
                break
        valids += status
    return valids


# Part 2

# def count_valid_passport_pt2(input_txt):
#     """Docstring TK"""
#     passports = []
#     for groupings in input_txt:
#         full_entries = re.split(r"\s", groupings)
#         passport = dict(x.split(":") for x in full_entries)
#         passports.append(passport)

#     valids = 0
#     for individual in passports:
#         status = 1
#         if individual["byr"] not in range(1920, 2003):
#             status = 0

#         valids += status
#     return valids


if __name__ == "__main__":
    # Input Data
    with open("./input.txt") as f:
        data = f.read()
    data_input = split_on_empty_lines(data)

    print(f"Part 1: {count_valid_passport_pt1(data_input, REQUIRED_FIELDS_1)}")
    # print(f"Part 2: {count_valid_passport_pt2(data_input, REQUIRED_FIELDS_1)}")
