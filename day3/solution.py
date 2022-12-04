def main():
    input_data = parse_input()
    rucksacks = [split_rucksack(rs) for rs in input_data]
    priority_items = [get_priority_item(*pair) for pair in rucksacks]
    priority_map = build_priority_map()

    # Part one
    pt1_total = sum([priority_map[itm] for itm in priority_items])
    print(pt1_total)

    # Part two

    groups = group_rucksacks_into_trios(input_data)
    badges = [determine_group_badge_type(grp) for grp in groups]
    pt2_total = sum([priority_map[typ] for typ in badges])
    print(pt2_total)


def parse_input():
    with open("input.txt") as FH:
        return [line.strip() for line in FH.readlines() if line]


def split_rucksack(line: str) -> tuple[set]:
    first_half = set(line[: len(line) // 2])
    second_half = set(line[len(line) // 2 :])

    return first_half, second_half


def group_rucksacks_into_trios(lines: list[str]) -> list[str]:
    groups = [lines[i : i + 3] for i in range(0, len(lines) + 1, 3)]
    # remove empty group
    groups = groups[:-1]
    return groups


def get_priority_item(fh: set, sh: set) -> str:
    # Assumes there's only one item in both
    item = fh.intersection(sh).pop()
    return item


def determine_group_badge_type(group: list[str]) -> str:
    group_as_sets = [set(bag) for bag in group]
    common_item = set.intersection(*group_as_sets).pop()
    return common_item


def build_priority_map() -> dict:
    lc_offset = 96
    uc_offset = 64
    uc_start = 26

    lc_map = {chr(i + lc_offset): i for i in range(1, 27)}
    uc_map = {chr(i + uc_offset): i + uc_start for i in range(1, 27)}

    return {**lc_map, **uc_map}


if __name__ == "__main__":
    main()
