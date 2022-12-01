def main():
    input_data = read_input("input.txt")
    groups = group_input(input_data)
    max_val = find_max(groups)
    print(max_val)


def read_input(path: str) -> str:
    with open(path) as FH:
        return FH.read()


def group_input(data: str) -> list[list[int]]:
    initial_groups = data.split("\n\n")
    sub_groups = [list(map(lambda v: int(v), g.split("\n"))) for g in initial_groups]
    return sub_groups


def find_max(groups: list[list[int]]) -> int:
    max_val = -1
    for group in groups:
        max_val = max(max_val, sum(group))
    return max_val


if __name__ == "__main__":
    main()
