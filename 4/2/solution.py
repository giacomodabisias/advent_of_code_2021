
INPUT_FILE = "input.txt"


def read_input() -> tuple[list[int], list[list[list[tuple[int, bool]]]]]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
    numbers = [int(num) for num in lines[0].strip().split(",")]

    counter = 0
    boards = []
    board = []
    for line in lines[1:]:
        if counter == 5:
            boards.append(board)
            board = []
            counter = 0
        if line not in ["\n", "\r\n"]:
            board.append([(int(num), False) for num in line.strip().split()])
            counter += 1
    boards.append(board)

    return numbers, boards


def print_board(board: list[list[tuple[int, bool]]]) -> None:
    for line in board:
        print(line)


def print_boards(boards: list[list[list[tuple[int, bool]]]]) -> None:
    for board in boards:
        print_board(board)
        print()


def is_winner(board: list[list[tuple[int, bool]]]) -> bool:
    for line in board:
        if all([value[1] for value in line]):
            return True

    for r_idx in range(0, 5):
        values = []
        for line in board:
            values.append(line[r_idx][1])
        if all(values):
            return True

    return False


def set_number_on_board(number: int, board: list[list[tuple[int, bool]]]) -> None:
    for l_idx, line in enumerate(board):
        for v_idx, value in enumerate(line):
            if value[0] == number:
                board[l_idx][v_idx] = (value[0], True)
                break


def get_sum_unmarked(board: list[list[tuple[int, bool]]]) -> int:
    total = 0
    for line in board:
        for value, truth in line:
            if not truth:
                total += value
    return total


if __name__ == "__main__":
    numbers, boards = read_input()
    print_boards(boards)
    winners = set()
    last_winning_board = None
    last_winning_number = None
    completed = False
    for number in numbers:
        if not completed:
            print(f"Current number {number}")
            print()
            for idx, board in enumerate(boards):
                set_number_on_board(number=number, board=board)
                if is_winner(board) and not idx in winners:
                    last_winning_board = idx
                    last_winning_number = number
                    winners.add(idx)
                if len(winners) == len(boards):
                    completed = True

    print(f"Winning number: {last_winning_number}")
    print(f"Winning board: {last_winning_board+1}")
    print()
    print_board(boards[last_winning_board])
    print()
    total_unmarked = get_sum_unmarked(boards[last_winning_board])
    print(f"Final product {total_unmarked*last_winning_number}")
    exit(0)



