from typing import Optional

INPUT_FILE = "input.txt"

points_lookup = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


def read_input() -> list[str]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


# Use a simple stack for this
def parse_line(line: str) -> tuple[bool, Optional[tuple[str, Optional[str]]]]:
    stack = []

    for _, symbol in enumerate(line):
        if symbol == "(" or symbol == "[" or symbol == "{" or symbol == "<":
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False, (symbol, None)
            else:
                current_top = stack.pop()
                if symbol == ")" and current_top != "(":
                    return False, (symbol, current_top)
                elif symbol == "}" and current_top != "{":
                    return False, (symbol, current_top)
                elif symbol == "]" and current_top != "[":
                    return False, (symbol, current_top)
                elif symbol == ">" and current_top != "<":
                    return False, (symbol, current_top)
    # In this case there were still parenthesis which we don't close but that's fine for now
    return True, None


if __name__ == "__main__":
    lines = read_input()
    corrupted_lines = []
    correct_lines = []
    points = 0

    for line in lines:
        parsable, error = parse_line(line)
        if not parsable:
            corrupted_lines.append(line)
            points += points_lookup[error[0]]
        else:
            correct_lines.append(line)

    print(f"Total points: {points}")

