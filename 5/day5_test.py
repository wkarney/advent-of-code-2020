from day5 import bp_to_seat_id


def test_examples_day5():
    """Test day 5 examples"""
    assert bp_to_seat_id("FBFBBFFRLR") == 357
    assert bp_to_seat_id("BFFFBBFRRR") == 567
    assert bp_to_seat_id("FFFBBBFRRR") == 119
    assert bp_to_seat_id("BBFFBBFRLL") == 820
