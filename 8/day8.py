#!/usr/bin/env python

"""
Advent of Code 2020, day 6
Will Karnasiewicz
"""


# Part 1
def accumulator_val_before_reloop(data_input):
    """Return the last accumulator value before boot code reloops"""
    i = 0
    accumulator = 0
    hit_indicies = []
    while i not in hit_indicies:
        hit_indicies.append(i)
        if data_input[i][0] == "acc":
            accumulator += int(data_input[i][1])
            i += 1
        elif data_input[i][0] == "jmp":
            i += int(data_input[i][1])
        elif data_input[i][0] == "nop":
            i += 1
        else:
            print("something is wrong with the input")
            break
    return accumulator


# Part 2


if __name__ == "__main__":
    # Input Data
    with open("./input.txt") as f:
        data = [line.rstrip("\n") for line in f]
        input_data = [group.split(" ") for group in data]

    print(f"Part 1: {accumulator_val_before_reloop(input_data)}")
