def main():
    input_data = parse_input()


def parse_input():
    with open("input.txt") as FH:
        return FH.readlines()


if __name__ == "__main__":
    main()
