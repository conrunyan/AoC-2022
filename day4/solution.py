def main():
    input_data = parse_input()
    pairs = PartOne.parse_pairs(input_data)
    total = PartOne.count_fully_contains(pairs)

    # Part two
    total_overlaps = PartTwo.count_overlaps(pairs)
    print(total)
    print(total_overlaps)


def parse_input():
    with open("input.txt") as FH:
        return FH.readlines()


class PartOne:
    @classmethod
    def parse_pairs(cls, input_lines: list[str]) -> list[tuple[list]]:
        return [cls.parse_pair(pair) for pair in input_lines]

    @classmethod
    def parse_pair(cls, pair: str) -> tuple[list]:
        lhs, rhs = pair.split(",")

        pair_lhs = [int(v) for v in lhs.split("-")]
        pair_rhs = [int(v) for v in rhs.split("-")]

        return pair_lhs, pair_rhs

    @classmethod
    def count_fully_contains(cls, pairs: list[tuple[list]]):
        count = 0
        for pair in pairs:
            if cls.lhs_contains_rhs(pair[0], pair[1]) or cls.lhs_contains_rhs(
                pair[1], pair[0]
            ):
                count += 1
        return count

    @classmethod
    def lhs_contains_rhs(cls, pair_lhs: list[int], pair_rhs: list[int]) -> bool:
        return (pair_lhs[0] <= pair_rhs[0]) and (pair_lhs[1] >= pair_rhs[1])


class PartTwo:
    @classmethod
    def lhs_overlaps_rhs(cls, lhs: list[int], rhs: list[int]) -> bool:
        lhs_values = {n for n in range(lhs[0], lhs[1] + 1)}
        rhs_values = {n for n in range(rhs[0], rhs[1] + 1)}

        overlapping = lhs_values.intersection(rhs_values)
        return len(overlapping) > 0

    @classmethod
    def count_overlaps(cls, pairs: list[tuple[list]]) -> int:
        return len([p for p in pairs if cls.lhs_overlaps_rhs(p[0], p[1])])


if __name__ == "__main__":
    main()
