INPUT_FILE = "input.txt"


def read_input() -> tuple[list[tuple[int, int]], list[tuple[str, int]]]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
    folds = []
    coords = []
    first_part = True
    for line in lines:
        if line in ["\n", "\r\n"]:
            first_part = False
            continue
        if first_part:
            coord = line.strip().split(",")
            coords.append((int(coord[0]), int(coord[1])))
        else:
            fold = line.strip().removeprefix("fold along ").split("=")
            folds.append((fold[0], int(fold[1])))

    return coords, folds


def print_board(board: list[list[str]]) -> None:
    for line in board:
        visible = []
        for value in line:
            if value == ".":
                visible.append(" ")
            else:
                visible.append(value)
        print(" ".join(visible))


def create_board(coords: list[tuple[int, int]]) -> list[list[str]]:
    max_col = max([coord[0] for coord in coords]) + 1
    max_row = max([coord[1] for coord in coords]) + 1
    board = [["." for _ in range(0, max_col)] for _ in range(0, max_row)]
    for coord in coords:
        col, row = coord
        board[row][col] = "#"
    return board


def sum_values(first: str, second: str) -> str:
    if first != second:
        return "#"
    else:
        return first


def create_new_board(board: list[list[str]], axis: str, value: int) -> list[list[str]]:
    if axis == "x":
        new_board = [["." for _ in range(0, value)] for _ in range(0, len(board))]
    else:
        new_board = [["." for _ in range(0, len(board[0]))] for _ in range(0, value)]
    return new_board


def fold(board: list[list[str]], fold_coords: tuple[str, int]) -> list[list[str]]:
    axis, value = fold_coords
    new_board = create_new_board(board=board, axis=axis, value=value)
    if axis == "x":
        for row in range(0, len(board)):
            for col in range(0, len(board[0]) - value - 1):
                new_board[row][col] = sum_values(board[row][col], board[row][len(board[0]) - col - 1])
    elif axis == "y":
        for row in range(0, len(board) - value - 1):
            for col in range(0, len(board[0])):
                new_board[row][col] = sum_values(board[row][col], board[len(board) - row - 1][col])
    else:
        raise ValueError("Unrecognized fold axis. Only x and y are supported")

    return new_board


def get_visible_dots(board: list[list[str]]) -> int:
    total = 0
    for line in board:
        for value in line:
            if value == "#":
                total += 1
    return total


if __name__ == "__main__":
    coords, folds = read_input()
    board = create_board(coords)

    for fold_coords in folds:
        board = fold(board=board, fold_coords=fold_coords)

    print_board(board)























