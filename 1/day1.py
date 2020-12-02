#!/usr/bin/env python

"""
Advent of Code 2020, day 1
Will Karnasiewicz
"""

import itertools
import math


# Parts 1 and 2


def expense_report_pairs(expense_txt, total, quantity):
    """Function for finding product of group of numbers in a list that sum to
    a specified quantity

    Parameters
    ----------
    expense_txt : list of ints
        The list of numbers to be analyzed
    total : int
        The sum that is to be achieved (e.g. 2020 for AoC 2020 Day 1)
    quantity : int
        The number of expenses that are summed to reach the quantity.

    Returns
    -------
    int
        The product of the group of numbers (size=quantity) that sums to the
        specified total.
    """
    for group in list(itertools.combinations(expense_txt, quantity)):
        if sum(group) == total:
            return math.prod(group)
    raise Exception("No solution found!")


if __name__ == "__main__":
    # Input Data
    with open("./input.txt") as f:
        input_list = [int(line.rstrip("\n")) for line in f]

    print(f"Part 1: {expense_report_pairs(input_list, 2020, 2)}")
    print(f"Part 2: {expense_report_pairs(input_list, 2020, 3)}")
