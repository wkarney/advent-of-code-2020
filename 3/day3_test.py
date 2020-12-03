from day3 import count_trees

test_input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def test_examples():
    """Test day 3  examples"""
    assert count_trees(test_input, start_pt=(0, 0), right_dist=1, down_dist=1) == 2
    assert count_trees(test_input, start_pt=(0, 0), right_dist=3, down_dist=1) == 7
    assert count_trees(test_input, start_pt=(0, 0), right_dist=5, down_dist=1) == 3
    assert count_trees(test_input, start_pt=(0, 0), right_dist=7, down_dist=1) == 4
    assert count_trees(test_input, start_pt=(0, 0), right_dist=1, down_dist=2) == 2
