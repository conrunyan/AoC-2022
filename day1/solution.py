def main():
    input_data = read_input("input.txt")
    groups = group_input(input_data)
    max_val = find_max(groups)
    top_three = find_top_three(groups)
    print(max_val)
    print(sum(top_three))


def read_input(path: str) -> str:
    with open(path) as FH:
        return FH.read()


def group_input(data: str) -> list[list[int]]:
    initial_groups = data.split("\n\n")
    sub_groups = [list(map(lambda v: int(v), g.split("\n"))) for g in initial_groups]
    return sub_groups


def find_top_three(groups: list[list[int]]) -> list[int]:
    sums = sorted([sum(grp) for grp in groups])
    return sums[-3:]


def find_max(groups: list[list[int]]) -> int:
    max_val = -1
    for group in groups:
        max_val = max(max_val, sum(group))
    return max_val


if __name__ == "__main__":
    main()
