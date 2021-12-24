
INPUT_FILE = "input.txt"
flashes = 0


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


def increase_values(board: list[list[int]]) -> None:
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            board[row][col] += 1


def adjacent(board: list[list[int]], row: int, col: int) -> list[tuple[int, int]]:
    neighbours = []
    for idx in [-1, 0, 1]:
        for idy in [-1, 0, 1]:
            if idx != 0 or idy != 0:
                if 0 <= row + idx < len(board) and 0 <= col + idy < len(board[0]):
                    neighbours.append((row + idx, col + idy))
    return neighbours


def flash(board: list[list[int]], row: int, col: int, flashing_board: list[list[bool]]) -> None:
    global flashes
    if board[row][col] > 9 and flashing_board[row][col] is False:
        board[row][col] = 0
        flashing_board[row][col] = True
        flashes += 1
        neighbours = adjacent(board=board, row=row, col=col)
        for neighbour in neighbours:
            board[neighbour[0]][neighbour[1]] += 1
            flash(board=board, row=neighbour[0], col=neighbour[1], flashing_board=flashing_board)
        for row in range(0, len(flashing_board)):
            for col in range(0, len(flashing_board[0])):
                if flashing_board[row][col] is True:
                    board[row][col] = 0


def light_up(board: list[list[int]], flashing_board: list[list[bool]]) -> None:
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            flash(board=board, row=row, col=col, flashing_board=flashing_board)


def get_new_board(board: list[list[int]]) -> list[list[bool]]:
    flashing_board = []
    for row in range(0, len(board)):
        flashing_board.append([])
        for col in range(0, len(board[0])):
            flashing_board[row].append(False)
    return flashing_board


def run_step(board: list[list[int]]) -> None:
    flashing_board = get_new_board(board)
    increase_values(board)
    light_up(board=board, flashing_board=flashing_board)


if __name__ == "__main__":
    board = read_input()

    flashes = 0
    for step in range(0, 100):
        run_step(board=board)

    print(f"total amount of flashes: {flashes}")













