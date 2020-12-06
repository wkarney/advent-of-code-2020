#!/usr/bin/env python

"""
Advent of Code 2020, day 6
Will Karnasiewicz
"""

import collections
import re


# Part 1
def count_sum_of_unique_yes_answers(input_txt):
    """Function for calculating sum of questions to which someone in a group
    answered "yes" on customs form from AoC 2020 Day 6 Part 2

    Parameters
    ----------
    input_txt : list of strings where each entry is a group of people waiting at customs

    Returns
    -------
    int
        The aggregate number of questions to which anyone in a group answered "yes."
    """
    count = 0
    for group in input_txt:
        count += len(set(re.findall(r"[a-zA-Z]", group)))
    return count


# Part 2
def count_sum_of_universal_yes_answers(input_txt):
    """Function for calculating sum of questions to which everyone in a group
    answered "yes" on customs form from AoC 2020 Day 6 Part 2

    Parameters
    ----------
    input_txt : list of strings where each entry is a group of people waiting at customs

    Returns
    -------
    int
        The aggregate number of questions to which everyone in a group answered "yes."
    """
    count = 0
    group_list = [group.split("\n") for group in input_txt]
    for group in group_list:
        if len(group) == 1:
            count += len(group[0])
        else:
            freq = collections.Counter("".join(group))
            count += len([k for k in freq if freq[k] == len(group)])

    return count


if __name__ == "__main__":
    # Input Data
    with open("./input.txt") as f:
        data = f.read()
    data_input = re.split(r"(?:\r?\n){2,}", data.strip())

    print(f"Part 1: {count_sum_of_unique_yes_answers(data_input)}")
    print(f"Part 2: {count_sum_of_universal_yes_answers(data_input)}")
