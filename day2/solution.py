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

PART_2_MAPPINGS = {
    "X": "LOST",
    "Y": "DRAW",
    "Z": "WIN",
}


MATCH_STATES = {
    ("A", "Y"): "WIN",
    ("B", "Z"): "WIN",
    ("C", "X"): "WIN",
    ("A", "X"): "DRAW",
    ("B", "Y"): "DRAW",
    ("C", "Z"): "DRAW",
    ("A", "Z"): "LOST",
    ("B", "X"): "LOST",
    ("C", "Y"): "LOST",
}


def main():
    input_data = parse_input("input.txt")
    score = sum([determine_match_score(match) for match in input_data])
    pt2_score = sum([determine_match_score_pt2(match) for match in input_data])
    print("Part one", score)
    print("Part two", pt2_score)


def parse_input(path: str) -> list[tuple[str]]:
    with open(path) as FH:
        return [tuple(line.split()) for line in FH.readlines()]


def determine_match_score(match: tuple[str]) -> int:
    match_points = 0
    if match_state := MATCH_STATES.get(match):
        match_points = OUTCOME_SCORES[match_state]

    shape_points = SHAPE_SCORES[match[1]]

    return match_points + shape_points


def determine_match_score_pt2(match: tuple[str]) -> int:
    desired_outcome = PART_2_MAPPINGS[match[1]]
    new_state = get_new_match_states(MATCH_STATES)
    opponent_shape = match[0]

    # What shape should we use?
    needed_shape = new_state[(opponent_shape, desired_outcome)]

    new_match = (opponent_shape, needed_shape)
    return determine_match_score(new_match)


def get_new_match_states(states: dict[tuple, str]) -> dict[tuple, str]:
    """
    Swaps the second piece of the matchstate tuple and the match result
    """
    new_state = {}
    for match_state, result in states.items():
        new_key = (match_state[0], result)
        new_val = match_state[1]
        new_state[new_key] = new_val

    return new_state


if __name__ == "__main__":
    main()
