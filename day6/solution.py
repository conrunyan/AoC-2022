def find_start_of_packet(stream: str, window_size: int = 4) -> int:
    window = []
    window_size = window_size
    for idx in range(len(stream) - window_size):
        window = set(stream[idx : idx + window_size])
        if len(window) == window_size:
            return idx + window_size
    return -1


def parse_input():
    with open("input.txt") as FH:
        return FH.read()


def part_1(input_data: str):
    result = find_start_of_packet(input_data)
    print("PART 1:", result)


def part_2(input_data: str):
    result = find_start_of_packet(input_data, window_size=14)
    print("PART 2:", result)


def main():
    input_data = parse_input()
    part_1(input_data)
    part_2(input_data)


if __name__ == "__main__":
    main()
