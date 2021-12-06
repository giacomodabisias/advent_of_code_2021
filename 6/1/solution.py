
INPUT_FILE = "input.txt"


def read_input() -> list[int]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
    initial_fishes = [int(num) for num in lines[0].strip().split(",")]
    return initial_fishes

if __name__ == "__main__":
    fishes = read_input()

    for days in range(0, 80):
        to_append = []
        for idx, fish in enumerate(fishes):
            if fish == 0:
                to_append.append(8)
                fishes[idx] = 6
            else:
                fishes[idx] -= 1
        fishes.extend(to_append)

    print(len(fishes))











