from typing import List

INPUT_FILE = "input.txt"


def read_input() -> List[int]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    return [int(line.strip()) for line in lines]


def current_window(values, index):
    return sum(values[index: index+3])


if __name__ == "__main__":
    depths = read_input()
    increases = 0
    prev_depth = sum(depths[:3])

    for idx in range(1, len(depths)-1):
        aggregated_depth = current_window(depths, idx)
        if aggregated_depth > prev_depth:
            increases += 1
        prev_depth = aggregated_depth

    print(increases)
