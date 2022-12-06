from solution import PartOne, PartTwo


def test_compare_contains():
    pair = ([1, 4], [2, 3])

    assert PartOne.lhs_contains_rhs(pair[0], pair[1]) is True
    assert PartOne.lhs_contains_rhs(pair[1], pair[0]) is False


def test_pairs_overlap():
    assert PartTwo.lhs_overlaps_rhs([2, 4], [6, 8]) is False
    assert PartTwo.lhs_overlaps_rhs([2, 3], [4, 5]) is False
    assert PartTwo.lhs_overlaps_rhs([5, 7], [7, 9]) is True
    assert PartTwo.lhs_overlaps_rhs([2, 8], [3, 7]) is True
    assert PartTwo.lhs_overlaps_rhs([6, 6], [4, 6]) is True
    assert PartTwo.lhs_overlaps_rhs([2, 6], [4, 8]) is True
