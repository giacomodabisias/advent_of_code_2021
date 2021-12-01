from typing import List

INPUT_FILE = "test.txt"


def read_input() -> List[int]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    return [int(line.strip()) for line in lines]


if __name__ == "__main__":
    depths = read_input()
    increases = 0
    prev_depth = depths[0]

    for depth in depths[1:]:
        if depth > prev_depth:
            increases += 1
        prev_depth = depth

    print(increases)
