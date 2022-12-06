import pytest
from solution import Stacks, CommandUtils, Crane


@pytest.fixture
def sample_stacks():
    return [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
    ]

@pytest.fixture
def sample_stacks_first_move():
    return [
        "[D]        ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
    ]


@pytest.fixture
def sample_commands():
    return [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]


def test_build_stacks(sample_stacks):
    expected = {"1": ["Z", "N"], "2": ["M", "C", "D"], "3": ["P"]}
    stacks = Stacks(sample_stacks)
    assert expected == stacks


def test_parse_commands(sample_commands):
    expected = [("1", "2", "1"), ("3", "1", "3"), ("2", "2", "1"), ("1", "1", "2")]
    result = CommandUtils.parse_commands(sample_commands)
    assert expected == result


def test_stacks_move_boxes(sample_stacks, sample_stacks_first_move):
    stacks = Stacks(sample_stacks)
    stacks.build_stacks(sample_stacks)
    moved_stacks = {}
