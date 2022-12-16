import pytest

from solution import get_border_tree_count, Grid, count_visible_trees


@pytest.fixture
def sample_input():
    return [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]


def test_get_border_tree_count(sample_input):
    assert get_border_tree_count(sample_input) == 16


def test_get_trees_up(sample_input):
    grid = Grid(sample_input)
    expected = [5, 0]
    trees = grid.get_trees(2, 1, "up")
    assert expected == trees


def test_get_trees_down(sample_input):
    grid = Grid(sample_input)
    expected = [5, 3]
    trees = grid.get_trees(2, 2, "down")
    assert expected == trees


def test_get_trees_right(sample_input):
    grid = Grid(sample_input)
    expected = [5, 1, 2]
    trees = grid.get_trees(1, 1, "right")
    assert expected == trees


def test_get_trees_right_2_3(sample_input):
    grid = Grid(sample_input)
    expected = [2]
    trees = grid.get_trees(2, 3, "right")
    assert expected == trees


def test_get_trees_left(sample_input):
    grid = Grid(sample_input)
    expected = [5, 6]
    trees = grid.get_trees(2, 2, "left")
    assert expected == trees


def test_count_visible_trees(sample_input):
    grid = Grid(sample_input)
    count, vis_trees = count_visible_trees(grid)
    assert count == 21


def test_count_visible_trees(sample_input):
    grid = Grid(sample_input)
    score = grid.get_scenic_score(3, 2)
    assert score == 8

def test_count_visible_trees(sample_input):
    grid = Grid(sample_input)
    score = grid.get_scenic_score(0, 0)
    assert score == 0
