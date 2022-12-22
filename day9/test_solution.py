import pytest

from solution import Bridge, execute_movements


@pytest.fixture
def sample_commands():
    return [
        ("R", 4),
        ("U", 4),
        ("L", 3),
        ("D", 1),
        ("R", 4),
        ("D", 1),
        ("L", 5),
        ("R", 2),
    ]


def test_execute_movements(sample_commands):
    br = Bridge()
    space_count = execute_movements(sample_commands, br)
    assert space_count == 13


def test_head_movements():
    br = Bridge()

    assert br.head.coords == (0, 0)

    br.move_head("left")
    br.move_head("left")
    assert br.head.coords == (-2, 0)

    br.move_head("right")
    br.move_head("up")
    br.move_head("up")
    br.move_head("down")
    br.move_head("left")
    assert br.head.coords == (-2, 1)


def test_tail_movements_up():
    br = Bridge()

    assert br.head.coords == (0, 0)
    assert br.tail.coords == (0, 0)

    br.move_head("up")
    assert br.head.coords == (0, 1)
    assert br.tail.coords == (0, 0)

    br.move_head("up")
    assert br.head.coords == (0, 2)
    assert br.tail.coords == (0, 1)


def test_tail_movements_down():
    br = Bridge()

    assert br.head.coords == (0, 0)
    assert br.tail.coords == (0, 0)

    br.move_head("down")
    assert br.head.coords == (0, -1)
    assert br.tail.coords == (0, 0)

    br.move_head("down")
    assert br.head.coords == (0, -2)
    assert br.tail.coords == (0, -1)


def test_tail_movements_left():
    br = Bridge()

    assert br.head.coords == (0, 0)
    assert br.tail.coords == (0, 0)

    br.move_head("left")
    assert br.head.coords == (-1, 0)
    assert br.tail.coords == (0, 0)

    br.move_head("left")
    assert br.head.coords == (-2, 0)
    assert br.tail.coords == (-1, 0)


def test_tail_movements_right():
    br = Bridge()

    assert br.head.coords == (0, 0)
    assert br.tail.coords == (0, 0)

    br.move_head("right")
    assert br.head.coords == (1, 0)
    assert br.tail.coords == (0, 0)

    br.move_head("right")
    assert br.head.coords == (2, 0)
    assert br.tail.coords == (1, 0)


def test_tail_movements_du_right():
    br = Bridge()

    br.move_head("up")
    br.move_head("right")
    br.move_head("right")
    assert br.head.coords == (2, 1)
    assert br.tail.coords == (1, 1)

    br._reset()

    br.move_head("right")
    br.move_head("up")
    br.move_head("up")
    assert br.head.coords == (1, 2)
    assert br.tail.coords == (1, 1)


def test_tail_movements_du_left():
    br = Bridge()

    br.move_head("up")
    br.move_head("left")
    br.move_head("left")
    assert br.head.coords == (-2, 1)
    assert br.tail.coords == (-1, 1)

    br._reset()

    br.move_head("left")
    br.move_head("up")
    br.move_head("up")
    assert br.head.coords == (-1, 2)
    assert br.tail.coords == (-1, 1)


def test_tail_movements_dd_right():
    br = Bridge()

    br.move_head("down")
    br.move_head("right")
    br.move_head("right")
    assert br.head.coords == (2, -1)
    assert br.tail.coords == (1, -1)

    br._reset()

    br.move_head("right")
    br.move_head("down")
    br.move_head("down")
    assert br.head.coords == (1, -2)
    assert br.tail.coords == (1, -1)


def test_tail_movements_dd_leftt():
    br = Bridge()

    br.move_head("down")
    br.move_head("left")
    br.move_head("left")
    assert br.head.coords == (-2, -1)
    assert br.tail.coords == (-1, -1)

    br._reset()

    br.move_head("left")
    br.move_head("down")
    br.move_head("down")
    assert br.head.coords == (-1, -2)
    assert br.tail.coords == (-1, -1)
