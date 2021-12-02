from enum import Enum, auto
from dataclasses import dataclass

INPUT_FILE = "input.txt"


class Move(Enum):
    up = auto()
    down = auto()
    forward = auto()
    aim = auto()


@dataclass(frozen=True)
class Movement:
    direction: Move
    amount: int


def read_input() -> list[Movement]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    moves = [(line.strip().split()[0], int(line.strip().split()[1])) for line in lines]
    enum_moves = []
    for move in moves:
        if move[0] == "up":
            enum_moves.append(Movement(direction=Move.up, amount=move[1]))
        elif move[0] == "down":
            enum_moves.append(Movement(direction=Move.down, amount=move[1]))
        elif move[0] == "forward":
            enum_moves.append(Movement(direction=Move.forward, amount=move[1]))
        elif move[0] == "aim":
            enum_moves.append(Movement(direction=Move.aim, amount=move[1]))
        else:
            raise ValueError(f"Unsupported move {move[0]}")

    return enum_moves


if __name__ == "__main__":
    movements = read_input()
    x_pos = 0
    y_pos = 0
    aim = 0

    for move in movements:
        if move.direction == Move.up:
            aim -= move.amount
        elif move.direction == Move.down:
            aim += move.amount
        elif move.direction == Move.forward:
            x_pos += move.amount
            y_pos += aim * move.amount
        else:
            raise ValueError(f"Unsupported move at runtime {move.direction}")

    print(f"Final position x:{x_pos}, y:{y_pos}")
    print(f"Final output {x_pos*y_pos}")