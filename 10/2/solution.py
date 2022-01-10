from typing import Optional

INPUT_FILE = "input.txt"

points_lookup = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def read_input() -> list[str]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


# Use a simple stack for this
def parse_line(line: str) -> tuple[bool, Optional[tuple[str, Optional[str]]], Optional[list[str]]]:
    stack = []

    for _, symbol in enumerate(line):
        if symbol == "(" or symbol == "[" or symbol == "{" or symbol == "<":
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False, (symbol, None), None
            else:
                current_top = stack.pop()
                if symbol == ")" and current_top != "(":
                    return False, (symbol, current_top), None
                elif symbol == "}" and current_top != "{":
                    return False, (symbol, current_top), None
                elif symbol == "]" and current_top != "[":
                    return False, (symbol, current_top), None
                elif symbol == ">" and current_top != "<":
                    return False, (symbol, current_top), None
    # In this case there were still parenthesis which we don't close but that's fine for now
    return True, None, stack


def complete_line(stack: str) -> str:
    missing_part = ""

    for symbol in stack[::-1]:
        if symbol == "(":
            missing_part += ")"
        elif symbol == "{":
            missing_part += "}"
        elif symbol == "[":
            missing_part += "]"
        elif symbol == "<":
            missing_part += ">"

    return missing_part


def compute_points(string: str) -> int:
    total_score = 0
    for symbol in string:
        total_score *= 5
        total_score += points_lookup[symbol]
    return total_score


if __name__ == "__main__":
    lines = read_input()
    corrupted_lines = []
    incomplete_lines = []
    points = []

    for line in lines:
        parsable, error, stack = parse_line(line)
        if not parsable:
            corrupted_lines.append(line)
        else:
            incomplete_lines.append(stack)

    for incomplete_line in incomplete_lines:
        missing_part = complete_line(incomplete_line)
        points.append(compute_points(missing_part))

    points.sort()
    print(f"Middle point: {points[len(points)//2]}")

