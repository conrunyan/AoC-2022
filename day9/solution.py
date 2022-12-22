def parse_input():
    with open("input.txt") as FH:
        return [line.strip().split() for line in FH.readlines()]


SHORT_HAND = {
    "R": "right",
    "U": "up",
    "L": "left",
    "D": "down",
}


DIRECTIONS = {
    "up": (0, 1),
    "down": (0, -1),
    "left": (-1, 0),
    "right": (1, 0),
    "du-right": (1, 1),
    "du-left": (-1, 1),
    "dd-right": (1, -1),
    "dd-left": (-1, -1),
}

# Series of relative x, y coords to determine
# where the tail should move.
# i.e. if the head is (0, 2) away from the tail, the tail moves right one.
TAIL_MOVEMENTS = {
    (2, 0): "right",
    (-2, 0): "left",
    (0, 2): "up",
    (0, -2): "down",
    (1, 2): "du-right",
    (2, 1): "du-right",
    (-1, 2): "du-left",
    (-2, 1): "du-left",
    (1, -2): "dd-right",
    (2, -1): "dd-right",
    (-1, -2): "dd-left",
    (-2, -1): "dd-left",
}


class Spot:
    def __init__(self):
        self.x = 0
        self.y = 0

    @property
    def coords(self):
        return (self.x, self.y)

    def move(self, x: int, y: int):
        self.x += x
        self.y += y


class Bridge:
    def __init__(self):
        self.head = Spot()
        self.tail = Spot()
        self.tail_places = {(0, 0)}

    def _reset(self):
        self.head = Spot()
        self.tail = Spot()

    def _move_spot(self, thing: Spot, direction: str) -> tuple[int, int]:
        change = DIRECTIONS[direction]
        thing.move(*change)
        return thing.coords

    def move_head(self, direction: str) -> tuple[int, int]:
        self._move_spot(self.head, direction)
        self.move_tail()

    def move_tail(self) -> tuple[int, int]:
        # (6, 4)
        # (4, 4)

        head_tail_x_diff = self.head.x - self.tail.x
        head_tail_y_diff = self.head.y - self.tail.y
        ht_diff = (head_tail_x_diff, head_tail_y_diff)

        if ht_diff in TAIL_MOVEMENTS:
            move = TAIL_MOVEMENTS[ht_diff]
            new_coords = self._move_spot(self.tail, move)
            self.tail_places.add(new_coords)


def execute_movements(input_data: list[list], bridge: Bridge) -> int:
    for command in input_data:
        sh_dir, count = command
        direction = SHORT_HAND[sh_dir]
        for _ in range(int(count)):
            bridge.move_head(direction)

    return len(bridge.tail_places)


def part_1(input_data):
    br = Bridge()
    space_count = execute_movements(input_data, br)
    print("PART 1:", space_count)


def part_2(input_data):
    pass


def main():
    input_data = parse_input()
    part_1(input_data)
    part_2(input_data)


if __name__ == "__main__":
    main()
