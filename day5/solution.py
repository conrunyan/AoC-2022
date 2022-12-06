import re
from collections import UserDict


def main():
    stack_data, command_data = parse_input()
    print(stack_data, command_data)


class Stacks(UserDict):
    def __init__(self, stack_input: list[str], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.build_stacks(stack_input)

    def _get_chars_from_line(self, line: str) -> list[str]:
        return [line[n] for n in range(1, len(line), 4)]

    def build_stacks(self, stack_input: list[str]):
        # Build it from the bottom up
        rev_lines = list(reversed(stack_input))
        stack_names = self._get_chars_from_line(rev_lines[0])

        for name in stack_names:
            self[name] = []

        for line in rev_lines[1:]:
            line_chars = self._get_chars_from_line(line)
            for idx, val in enumerate(line_chars):
                if val != " ":
                    self[str(idx + 1)].append(val)


class Crane:
    @classmethod
    def move_boxes(
        cls, stacks: Stacks, move_count: str, move_from: str, move_to: str
    ) -> Stacks:
        for n in range(int(move_count)):
            box = stacks[move_from].pop()
            stacks[move_to].append(box)

        return stacks


class CommandUtils:
    @classmethod
    def parse_commands(self, command_data: list[str]) -> list[list]:
        re_commands = r"move (\d+) from (\d+) to (\d+)"
        return [re.search(re_commands, line).groups() for line in command_data]


def parse_input():
    with open("input.txt") as FH:
        lines = FH.readlines()

    split_idx = lines.index("\n")
    stack_data = lines[:split_idx]
    command_data = lines[split_idx + 1 :]

    return stack_data, command_data


if __name__ == "__main__":
    main()
