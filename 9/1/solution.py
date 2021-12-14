
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


if __name__ == "__main__":
    board = read_input()
    print_board(board)
    low_points = get_low_points(board)
    low_points_sum = sum([1+board[low_point[0]][low_point[1]] for low_point in low_points])
    print(low_points_sum)












