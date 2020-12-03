#!/usr/bin/env python

"""
Advent of Code 2020, day 3
Will Karnasiewicz
"""

# Part 1


def count_trees(input_txt, start_pt, right_dist, down_dist):
    """Function for calculating number of valid passwords at sled rental place

    Parameters
    ----------
    input_txt : list of strings where each item in the list is a row of positions,
    with either no tree '.' or a tree '#' at each position

    start_pt : a tuple that represents the starting location of your journey

    right_dist : an integer that is the rightward distance of your toboggan for each move

    down_dist : an integer that is the downward distance of your toboggan for each move

    Returns
    -------
    int
        The number of trees encountered in your journey
    """
    # Using arboreal genetics and biome stability, create rightward expansion of trees
    duration = len(input_txt) / down_dist  # number of loops downward to finish
    new_growth = int(
        -((-duration * right_dist) // len(input_txt[0]))
    )  # number of duplications needed
    geography = []
    for line in input_txt:
        line = line * new_growth
        geography.append(line)

    row, col = start_pt
    tree = 0
    while row < len(geography) - 1:
        row += down_dist
        col += right_dist
        if geography[row][col] == "#":
            tree += 1
    return tree


if __name__ == "__main__":
    # Input Data
    with open("./input.txt") as f:
        input_list = [line.rstrip("\n") for line in f]

    print(
        f"Part 1: {count_trees(input_list, start_pt=(0,0), right_dist=3, down_dist=1)}"
    )

    SLOPE1 = count_trees(input_list, start_pt=(0, 0), right_dist=1, down_dist=1)
    SLOPE2 = count_trees(input_list, start_pt=(0, 0), right_dist=3, down_dist=1)
    SLOPE3 = count_trees(input_list, start_pt=(0, 0), right_dist=5, down_dist=1)
    SLOPE4 = count_trees(input_list, start_pt=(0, 0), right_dist=7, down_dist=1)
    SLOPE5 = count_trees(input_list, start_pt=(0, 0), right_dist=1, down_dist=2)

    print(f"Part 2: {SLOPE1 * SLOPE2 * SLOPE3 * SLOPE4 * SLOPE5}")
