#!/usr/bin/env python

"""
Advent of Code 2020, day 2
Will Karnasiewicz
"""

# Part 1


def count_valid_passwords(input_txt):
    """Function for calculating number of valid passwords at sled rental place

    Parameters
    ----------
    input_txt : list of strings formatted as 'int1-int2 letter: password'
        The list of passwords / policies combinations to be analyzed

    Returns
    -------
    int
        The number of valid passwords contained in the list
    """
    valids = 0
    for item in input_txt:
        policy, password = item.split(": ")
        letter = policy[-1]
        min_quantity, max_quantity = [
            int(item) for item in policy.split(" ")[0].split("-")
        ]

        if password.count(letter) in range(min_quantity, max_quantity + 1):
            valids += 1
    return valids


# Part 2


def count_officially_valid_passwords(input_txt):
    """Function for calculating number of valid passwords at sled rental place
    using The Official Toboggan Corporate Policy.

    Parameters
    ----------
    input_txt : list of strings formatted as 'int1-int2 letter: password'
        The list of passwords / policies combinations to be analyzed

    Returns
    -------
    int
        The number of valid passwords contained in the list
    """
    valids = 0
    for item in input_txt:
        policy, password = item.split(": ")
        letter = policy[-1]
        loc_1, loc_2 = [int(item) - 1 for item in policy.split(" ")[0].split("-")]
        if letter in [password[loc_1], password[loc_2]]:
            if (password[loc_1] == letter) and (password[loc_2] == letter):
                continue
            valids += 1
    return valids


if __name__ == "__main__":
    # Input Data
    with open("./input.txt") as f:
        input_list = [line.rstrip("\n") for line in f]

    print(f"Part 1: {count_valid_passwords(input_list)}")
    print(f"Part 2: {count_officially_valid_passwords(input_list)}")
