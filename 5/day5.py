#!/usr/bin/env python

"""
Advent of Code 2020, day 5
Will Karnasiewicz
"""


def bp_to_seat_id(boarding_pass):
    """Function for calculating boarding pass from binary code in AoC 2020 Day 5

    Parameters
    ----------
    input_txt : list of strings of the following form:
    7 characters of either "F" or "B" representing rows 0-127, and
    3 characters of either "L" or "R" representing columns 0-7.

    Returns
    -------
    int
        The seat id of the seat specified by the boarding pass.
    """
    boarding_pass = (
        boarding_pass.replace("F", "0")
        .replace("B", "1")
        .replace("L", "0")
        .replace("R", "1")
    )
    row, col = int(boarding_pass[0:7], 2), int(boarding_pass[7:], 2)
    return row * 8 + col


if __name__ == "__main__":
    # Input Data
    with open("./input.txt") as f:
        input_list = [line.rstrip("\n") for line in f]

    print(f"Part 1: { max([bp_to_seat_id(bp) for bp in input_list])}")

    plane_seat_ids = sorted([bp_to_seat_id(bp) for bp in input_list])

    for i, j in enumerate(plane_seat_ids):
        if plane_seat_ids[i] == plane_seat_ids[i - 1] + 2:
            print(f"Part 2: {plane_seat_ids[i]-1}")
