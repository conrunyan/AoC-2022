import re
from collections import UserDict


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

    def get_top_of_stacks(self):
        combined_top = ""
        for stack in self.values():
            top = stack[-1]
            combined_top += top
        return combined_top


class Crane:
    @classmethod
    def move_boxes(
        cls, stacks: Stacks, move_count: str, move_from: str, move_to: str
    ) -> Stacks:
        for n in range(int(move_count)):
            box = stacks[move_from].pop()
            stacks[move_to].append(box)

        return stacks

    @classmethod
    def move_boxes_keep_order(
        cls, stacks: Stacks, move_count: str, move_from: str, move_to: str
    ) -> Stacks:
        crane_storage = []
        for n in range(int(move_count)):
            box = stacks[move_from].pop()
            crane_storage.append(box)

        for box in reversed(crane_storage):
            stacks[move_to].append(box)

        return stacks

    @classmethod
    def execute_crane_commands(
        cls,
        stacks: Stacks,
        commands: list[tuple[str]],
    ) -> Stacks:
        for cmd in commands:
            stacks = cls.move_boxes(stacks, *cmd)
        return stacks

    @classmethod
    def execute_crane_commands_keep_order(
        cls,
        stacks: Stacks,
        commands: list[tuple[str]],
    ) -> Stacks:
        for cmd in commands:
            stacks = cls.move_boxes_keep_order(stacks, *cmd)
        return stacks


class CommandUtils:
    @classmethod
    def parse_commands(cls, command_data: list[str]) -> list[list]:
        re_commands = r"move (\d+) from (\d+) to (\d+)"
        return [re.search(re_commands, line).groups() for line in command_data]


def part_1(stack_data: Stacks, commands: list[tuple[str]]):
    stacks = Stacks(stack_data)
    stacks = Crane.execute_crane_commands(stacks, commands)
    answer = stacks.get_top_of_stacks()
    print("PART 1:", answer)


def part_2(stack_data: Stacks, commands: list[tuple[str]]):
    stacks = Stacks(stack_data)
    stacks = Crane.execute_crane_commands_keep_order(stacks, commands)
    answer = stacks.get_top_of_stacks()
    print("PART 2:", answer)


def parse_input():
    with open("input.txt") as FH:
        lines = FH.readlines()

    split_idx = lines.index("\n")
    stack_data = lines[:split_idx]
    command_data = lines[split_idx + 1 :]

    return stack_data, command_data


def main():
    stack_data, command_data = parse_input()
    commands = CommandUtils.parse_commands(command_data)

    part_1(stack_data, commands)
    part_2(stack_data, commands)


if __name__ == "__main__":
    main()
