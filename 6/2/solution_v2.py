from collections import defaultdict

INPUT_FILE = "test.txt"

def read_input() -> list[int]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
    return [int(num) for num in lines[0].strip().split(",")]


if __name__ == "__main__":
    states = defaultdict(lambda: 0)
    starting_population = read_input()
    days = 256

    for starting_p in starting_population:
        states[starting_p] += 1

    for day in range(0, days):
        new_states = [0] * 9
        new_states[8] = states[0]
        new_states[6] = states[0]
        for idx in range(8):
            new_states[idx] += states[idx+1]
        states = new_states

    print(sum(states))




