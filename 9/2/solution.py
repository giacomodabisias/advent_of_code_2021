import math

INPUT_FILE = "input.txt"


def read_input() -> list[list[int]]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
    board = []
    for line in lines:
        digits = line.strip()
        board.append([int(digit) for digit in digits])
    return board


def print_board(board: list[list[int]]) -> None:
    for line in board:
        print(line)


def is_low_point(row: int, col: int, board: list[list[int]]) -> bool:
    neighbours = []
    if 0 <= row + 1 < len(board) and 0 <= col < len(board[0]):
        neighbours.append((row + 1, col))
    if 0 <= row < len(board) and 0 <= col + 1 < len(board[0]):
        neighbours.append((row, col + 1))
    if 0 <= row - 1 < len(board) and 0 <= col < len(board[0]):
        neighbours.append((row - 1, col))
    if 0 <= row < len(board) and 0 <= col - 1 < len(board[0]):
        neighbours.append((row, col - 1))
    return all([board[row][col] < board[neighbour[0]][neighbour[1]] for neighbour in neighbours])


def get_low_points(board: list[list[int]]) -> list[tuple[int, int]]:
    low_points = []
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if is_low_point(row, col, board):
                low_points.append((row, col))
    return low_points


def find_low_neighbours(board: list[list[int]], low_point: tuple[int, int]) -> list[tuple[int, int]]:
    neighbours = []
    row, col = low_point
    current_point = board[row][col]
    if 0 <= row + 1 < len(board) and 0 <= col < len(board[0]) and board[row + 1][col] > current_point and board[row + 1][col] != 9:
        neighbours.append((row + 1, col))
    if 0 <= row < len(board) and 0 <= col + 1 < len(board[0]) and board[row][col + 1] > current_point and board[row][col + 1] != 9:
        neighbours.append((row, col + 1))
    if 0 <= row - 1 < len(board) and 0 <= col < len(board[0]) and board[row - 1][col] > current_point and board[row - 1][col] != 9:
        neighbours.append((row - 1, col))
    if 0 <= row < len(board) and 0 <= col - 1 < len(board[0]) and board[row][col - 1] > current_point and board[row][col - 1] != 9:
        neighbours.append((row, col - 1))
    return neighbours


def find_basin(board: list[list[int]], low_point: tuple[int, int]) -> list[tuple[int, int]]:

    visited = set()
    lower_points = [low_point]
    basin = []

    while len(lower_points) != 0:
        current = lower_points.pop()
        low_neighbours = find_low_neighbours(board, current)
        for low_neighbour in low_neighbours:
            if low_neighbour not in visited:
                lower_points.append(low_neighbour)
                basin.append(low_neighbour)
                visited.add(low_neighbour)
        if current not in visited:
            visited.add(current)
            basin.append(current)
        visited.add(current)

    return basin


if __name__ == "__main__":
    board = read_input()
    low_points = get_low_points(board)

    basins = []
    for low_point in low_points:
        basins.append(find_basin(board, low_point))

    basin_sum = [sum([1 for value in basin]) for basin in basins]
    basin_sum.sort(reverse=True)

    print(f"The 3 largest basins are {basin_sum[:3]}, prod: {math.prod(basin_sum[:3])}")
