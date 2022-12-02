MAPPING = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}


SHAPE_SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

OUTCOME_SCORES = {
    "LOST": 0,
    "DRAW": 3,
    "WIN": 6,
}

MATCH_STATES = {
    ("A", "Y"): "WIN",
    ("B", "Z"): "WIN",
    ("C", "X"): "WIN",
    ("A", "X"): "DRAW",
    ("B", "Y"): "DRAW",
    ("C", "Z"): "DRAW",
}


def main():
    input_data = parse_input("input.txt")
    score = sum([determine_match_score(match) for match in input_data])
    print(score)


def parse_input(path: str) -> list[tuple[str]]:
    with open(path) as FH:
        return [tuple(line.split()) for line in FH.readlines()]


def determine_match_score(match: tuple[str]) -> int:
    match_points = 0
    if match_state := MATCH_STATES.get(match):
        match_points = OUTCOME_SCORES[match_state]

    shape_points = SHAPE_SCORES[match[1]]

    return match_points + shape_points


if __name__ == "__main__":
    main()
