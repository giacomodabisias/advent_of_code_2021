from collections import defaultdict
import math

INPUT_FILE = "input.txt"


def read_input() -> tuple[str, dict]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    template = lines[0].strip()
    lines = lines[2:]
    rules = dict()
    for line in lines:
        parts = line.strip().split(" -> ")
        rules[parts[0]] = parts[1]

    return template, rules


def find_minmax_elements(template: dict[str, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    contents = defaultdict(lambda: 0)

    for key, value in template.items():
        contents[key[0]] += value
        contents[key[1]] += value


    max_element = float("-inf")
    max_key = ""
    min_element = float("inf")
    min_key = ""

    for key, value in contents.items():
        if value > max_element:
            max_element = value
            max_key = key
        if value < min_element:
            min_element = value
            min_key = key

    return (min_key, min_element), (max_key, max_element)


if __name__ == "__main__":
    template, rules = read_input()
    template_dict = defaultdict(lambda: 0)

    for idx in range(len(template) - 1):
        template_dict[template[idx:idx+2]] += 1

    for round in range(10):
        new_template_dict = defaultdict(lambda: 0)
        for key, value in template_dict.items():
            if key in rules:
                new_template_dict[key[0] + rules[key]] += value
                new_template_dict[rules[key] + key[1]] += value
            else:
                new_template_dict[key] += 1

        template_dict = new_template_dict

    min_element, max_element = find_minmax_elements(template_dict)
    print(f"MaxMin diff: {math.ceil((max_element[1] - min_element[1]) / 2 )}")




