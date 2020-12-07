#!/usr/bin/env python

"""
Advent of Code 2020, day 4
Will Karnasiewicz
"""

import re

REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# Part 1
def count_valid_passport_pt1(input_txt, required_fields):
    """Function for counting number of valid passports in a group for
    AOC 2020 Day 4 Pt 1
    """
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
def field_is_valid(k, v):
    """Function to determine whether a given passport field is valid"""
    if k == "byr":
        if int(v) in range(1920, 2003):
            return True
    elif k == "iyr":
        if int(v) in range(2010, 2021):
            return True
    elif k == "eyr":
        if int(v) in range(2020, 2031):
            return True
    elif k == "hgt":
        if v[-2:] == "cm":
            if int(v.split("cm")[0]) in range(150, 194):
                return True
            return False
        if v[-2:] == "in":
            if int(v.split("in")[0]) in range(59, 77):
                return True
            return False
        return False
    elif k == "hcl":
        return v[0] == "#" and len(re.findall(r"[a-zA-Z0-9]{6}", v[1:])) == 1
    elif k == "ecl":
        if v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True
        return False
    elif k == "pid":
        pid_digits = re.findall(r"[0-9]{9}$", v)
        if pid_digits != [] and len(v) == 9:
            return True
        return False
    elif k == "cid":
        return True
    return False


def count_valid_passport_pt2(input_txt, required_fields):
    """Function for counting number of valid passports in a group for
    AOC 2020 Day 4 Pt 2"""
    passports = []
    for groupings in input_txt:
        full_entries = re.split(r"\s", groupings)
        passport = dict(x.split(":") for x in full_entries)
        passports.append(passport)

    valids = 0
    for individual in passports:
        status = 1

        for item in required_fields:
            if item not in individual:
                status = 0
                break

        for key, value in individual.items():
            if not field_is_valid(key, value):
                status = 0
                break
        valids += status
    return valids


if __name__ == "__main__":
    # Input Data
    with open("./input.txt") as f:
        data = f.read()
    data_input = re.split(r"(?:\r?\n){2,}", data.strip())

    print(f"Part 1: {count_valid_passport_pt1(data_input, REQUIRED_FIELDS)}")
    print(f"Part 2: {count_valid_passport_pt2(data_input, REQUIRED_FIELDS)}")
