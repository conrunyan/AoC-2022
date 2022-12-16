import math

def parse_input():
    with open("input.txt") as FH:
        return [l.strip() for l in FH.readlines()]


class Grid:
    def __init__(self, input_lines: list[str]):
        self.grid = []
        for line in input_lines:
            col = []
            for char in line:
                col.append(int(char))
            self.grid.append(col)
        self.directions = ["up", "down", "left", "right"]

    def get_trees(self, start_row: int, start_col, direction: str) -> list[int]:
        trees = []
        if direction == "up":
            for n in range(start_row - 1, -1, -1):
                trees.append(self.grid[n][start_col])

        elif direction == "down":
            for n in range(start_row + 1, len(self.grid)):
                trees.append(self.grid[n][start_col])

        elif direction == "left":
            for n in range(start_col - 1, -1, -1):
                trees.append(self.grid[start_row][n])

        elif direction == "right":
            for n in range(start_col + 1, len(self.grid[start_col])):
                trees.append(self.grid[start_row][n])

        return trees

    def tree_is_visible(self, row: int, col: int) -> bool:
        tree_val = self.grid[row][col]
        return any(
            [
                tree_val > max(self.get_trees(row, col, direction))
                for direction in self.directions
            ]
        )

    def get_scenic_score(self, row: int, col: int) -> int:
        scores = []
        for direc in self.directions:
            trees = self.get_trees(row, col, direc)
            score = self.count_visible_trees(self.grid[row][col], trees)
            scores.append(score)
        
        return math.prod(scores)

    def count_visible_trees(self, tree_val: int, trees: list[int]) -> int:
        count = 0
        for tree in trees:
            if tree < tree_val:
                count += 1
            else:
                count += 1
                break
        return count


def get_border_tree_count(grid: list[str]):
    return len(grid) * 4 - 4


def count_visible_trees(grid: Grid) -> int:
    visible_trees = {}
    count = 0 + get_border_tree_count(grid.grid)
    for row_idx in range(1, len(grid.grid) - 1):
        for col_idx in range(1, len(grid.grid) - 1):
            if grid.tree_is_visible(row_idx, col_idx):
                visible_trees[(row_idx, col_idx)] = True
                count += 1
    return count, visible_trees


def calculate_best_scenic_score(grid: Grid) -> int:
    best_score = -1
    for row_idx in range(len(grid.grid)):
        for col_idx in range(len(grid.grid)):
            score = grid.get_scenic_score(row_idx, col_idx)
            best_score = max(score, best_score)
    return best_score


def part_1(input_data):
    grid = Grid(input_data)
    count, _ = count_visible_trees(grid)
    print("PART 1:", count)


def part_2(input_data):
    grid = Grid(input_data)
    score = calculate_best_scenic_score(grid)
    print("PART 2:", score)


def main():
    input_data = parse_input()
    part_1(input_data)
    part_2(input_data)


if __name__ == "__main__":
    main()
