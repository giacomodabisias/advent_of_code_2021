
INPUT_FILE = "solution.txt"


def read_input() -> list[tuple[tuple[int, int], tuple[int, int]]]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    vents = []

    for line in lines:
        tuples = line.strip().split("->")
        tuple_1 = int(tuples[0].strip().split(",")[1]), int(tuples[0].strip().split(",")[0])
        tuple_2 = int(tuples[1].strip().split(",")[1]), int(tuples[1].strip().split(",")[0])
        vents.append((tuple_1, tuple_2))

    return vents


def get_maxes(vents) -> tuple[int, int]:
    max_x = -1
    max_y = -1
    for vent in vents:
        max_x = max(max_x, vent[0][0])
        max_x = max(max_x, vent[1][0])
        max_y = max(max_y, vent[0][1])
        max_y = max(max_y, vent[1][1])
    return max_x, max_y


def print_board(board: list[list[int]]) -> None:
    for line in board:
        print(line)
        print()

def create_new_board(max_x: int, max_y: int) -> list[list[int]]:
    board = []
    for x in range(0, max_x+1):
        board.append([])
        for y in range(0, max_y+1):
            board[x].append(0)
    return board


def get_overlaps(board: list[list[int]]) -> int:
    overlaps = 0
    for line in board:
        for value in line:
            if value > 1:
                overlaps += 1
    return overlaps

def get_cells(vent_pair: tuple[tuple[int, int], tuple[int, int]]) -> list[tuple[int, int]]:
    cells = []
    vent_1, vent_2 = vent_pair
    x0, y0 = vent_1
    x1, y1 = vent_2
    if x0 == x1:
        if y0 < y1:
            for y_diff in range(y0, y1+1):
                cells.append((x0, y_diff))
        else:
            for y_diff in range(y1, y0+1):
                cells.append((x0, y_diff))
    elif y0 == y1:
        if x0 < x1:
            for x_diff in range(x0, x1+1):
                cells.append((x_diff, y0))
        else:
            for x_diff in range(x1, x0+1):
                cells.append((x_diff, y0))
    return cells


def update_board(board: list[list[int]], vent_pair: tuple[tuple[int, int], tuple[int, int]]) -> None:
    cells = get_cells(vent_pair)
    for cell in cells:
        x, y = cell
        board[x][y] += 1


if __name__ == "__main__":
    vent_pairs = read_input()
    max_x, max_y = get_maxes(vent_pairs)
    board = create_new_board(max_x=max_x, max_y=max_y)

    for vent_pair in vent_pairs:
        vent_1, vent_2 = vent_pair
        update_board(board=board, vent_pair=vent_pair)

    overlaps = get_overlaps(board)
    print(f"Found {overlaps} overlaps")








