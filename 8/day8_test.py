from day8 import accumulator_val_before_reloop

with open("8/ex1-input.txt") as f:
    data = [line.rstrip("\n") for line in f]
    ex_data = [group.split(" ") for group in data]


def test_example_day8_pt1():
    """Test day 8 pt 1 example"""
    assert accumulator_val_before_reloop(ex_data) == 5


# def test_example_day6_pt2():
#     """Test day 8 pt 2 example"""
#     assert accumulator_fixed_loop(ex_data2) == 8
