#!/usr/bin/env python

"""
Advent of Code 2020, day 7
Will Karnasiewicz
"""

import re


def input_to_rule_dict(input_data):
    """Docstring TK"""
    rule_dict = {}
    for bag_sentence in input_data:
        subject_bag, inner_bags = bag_sentence.split("bags contain")
        outer_color = " ".join(subject_bag.rsplit())
        inner_values = [
            " ".join(re.findall(r"[a-z]{2,}", segment))
            for segment in inner_bags.split("bag")
            if segment not in ["s.", ".", "\n"]
        ]
        if re.findall(r"[0-9]", inner_bags) == []:
            inner_counts = [0]
        else:
            inner_counts = [int(i) for i in re.findall(r"[0-9]", inner_bags)]
        rule_dict.update(
            {
                outer_color: {
                    inner_values[i]: inner_counts[i] for i in range(len(inner_values))
                }
            }
        )
    return rule_dict


def direct_bag_colors(color, rule_list):
    """Docstring TK"""
    return [k for k, v in rule_list.items() if color in v.keys()]


def count_outer_bag_options(color, rule_list):
    """Docstring TK"""
    outers = []
    new_colors = direct_bag_colors(color, rule_list)
    while new_colors != []:
        outers.extend(new_colors)
        sub_colors = []
        for colors in new_colors:
            sub_colors.extend(direct_bag_colors(colors, rule_list))
        new_colors = list(set(sub_colors))
    return len(set(outers))


# Part 2
def direct_bag_color_dict(color, rule_list):
    """Docstring TK"""
    # print([k for k, v in rule_list[color].items()])
    return rule_list[color].items()


def bag_contents(color, rule_list):
    """Docstring TK"""
    contents = direct_bag_color_dict(color, rule_list)
    print(contents)

    # while contents != {'no other': 0}:
    #         print(color)
    #         contents = direct_bag_color_dict(color, rule_list)
    #         print(contents)

    # counts = []
    # total = 0
    # for color in contents:
    #     sub_count = [contents[color]]
    #     sub_content = direct_bag_color_dict(color, rule_list)
    #     print(sub_count)
    #     print(sub_content)
    #     for item in sub_content:
    #         if item == 'no other':
    #             break
    #         sub_count.append(sub_content[item])


#         counts.extend(sub_count)
#         print(color)
#         print(counts)
#         total += math.prod(counts)
#     return total


# print(content)
# for color in contents.keys():
#     print(color)
#     count = 0
#     sub_colors = [k for k in rule_list[color].keys()]
#     sub_counts = [v for k, v in rule_list[color].items()]
#     inner_bags = {sub_colors[i]: sub_counts[i] for i in range(len(sub_colors))}
#     for color in inner_bags:
#         counts = inner_bags[color]
#         new_color =
#         while counts > 0:
#             p
#         print(color)
# for colors in sub_colors:
#     print(colors)
#     sub_colors2 = [k for k in rule_list[colors].keys()]
#     sub_counts2 = [v for k, v in rule_list[colors].items()]
#     print(sub_colors2)
#     print(sub_counts2)
#     while colors != ['no other']:
#         break
#     print(sub_colors2)
#     print(sub_counts2)
# # while sub_count != 0:
#     count += sub_count

# Quick: copy paste version: shiny gold bags contain 2 pale maroon bags,
# 5 pale purple bags, 4 posh brown bags, 1 dotted turquoise bag.

if __name__ == "__main__":
    # Input Data
    with open("./input.txt") as f:
        input_list = [line.rstrip("\n") for line in f]

    with open("./ex_pt2_input2.txt") as f:
        ex2_list = [line.rstrip("\n") for line in f]

    # print(input_to_rule_dict(input_list))
    print(direct_bag_color_dict("shiny gold", input_to_rule_dict(input_list)))

    print(
        f"Part 1:\
             {count_outer_bag_options('shiny gold', input_to_rule_dict(input_list))}"
    )

    # print(bag_contents('shiny gold', input_to_rule_dict(ex2_list)))
    print(f"Part 2: {bag_contents('shiny gold', input_to_rule_dict(input_list))}")
