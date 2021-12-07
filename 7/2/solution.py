import sys
INPUT_FILE = "input.txt"


def read_input() -> list[int]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
    return [int(num) for num in lines[0].strip().split(",")]


if __name__ == "__main__":
    initial_positions = read_input()
    max_pos = max(initial_positions)
    min_pos = min(initial_positions)

    best_fuel = sys.maxsize
    best_pos = -1

    for alignment_position in range(min_pos, max_pos + 1):
        fuel = 0
        for initial_position in initial_positions:
            distance = abs(initial_position - alignment_position)
            fuel += (distance * (distance + 1)) // 2
        if fuel < best_fuel:
            best_fuel = fuel
            best_pos = alignment_position

    print(f"Best position: {best_pos}")
    print(f"Best consumption: {best_fuel}")











