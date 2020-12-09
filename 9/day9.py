#!/usr/bin/env python

"""
Advent of Code 2020, day 9
Will Karnasiewicz
"""

import itertools


def find_pairs_that_sum(lst, target):
    """Helper function to find pairs that sum to a number"""
    return [pair for pair in itertools.combinations(lst, 2) if sum(pair) == target]


# Part 1
def find_first_invalid_value(data_input, preample_size):
    """Find first value that is not the sum of two of the most
    recent numbers given by the preamble size"""
    for i, val in enumerate(data_input):
        if i < preample_size:
            continue
        if find_pairs_that_sum(data_input[i - preample_size : i], val):
            continue
        return val


# Part 2
def find_pt2(data_input, invalid_value):
    """Find answer to part 2"""
    cumsum_data = list(itertools.accumulate(data_input))
    for i in range(len(data_input)):
        if cumsum_data[i] < invalid_value:
            continue
        for j in range(i):
            if cumsum_data[i] - cumsum_data[j] == invalid_value:
                return min(data_input[j + 1 : i + 1]) + max(data_input[j + 1 : i + 1])
    print("Something went wrong; encryption weakness not found")
    return None


if __name__ == "__main__":
    # Input Data
    with open("./input.txt") as f:
        input_data = [int(line) for line in f]

    first_invalid_value = find_first_invalid_value(input_data, 25)

    print(f"Part 1: {first_invalid_value}")
    print(f"Part 2: {find_pt2(input_data, first_invalid_value)}")
