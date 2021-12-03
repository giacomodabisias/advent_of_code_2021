
INPUT_FILE = "test.txt"


def to_bin(string: str) -> int:
    rev_string = string[::-1]
    output = 0
    for idx, bin_val in enumerate(rev_string):
        if bin_val == "1":
            output += 2**idx
    return output


def read_input() -> list[str]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
    return [(line.strip()) for line in lines]


if __name__ == "__main__":
    bins = read_input()
    values = []

    for bit in bins[0]:
        values.append({"0": 0, "1": 1})

    for bin_num in bins:
        for idx, bit in enumerate(bin_num):
            values[idx][bit] += 1

    gamma_rate = ""
    epsilon_rate = ""
    for value in values:
        if value["0"] > value ["1"]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    print(f"Gamma rate: {gamma_rate}")
    print(f"Epsilon rate: {epsilon_rate}")

    bin_gamma_rate = to_bin(gamma_rate)
    bin_epsilon_rate = to_bin(epsilon_rate)

    print(f"Bin Gamma rate: {bin_gamma_rate}")
    print(f"Bin Epsilon rate: {bin_epsilon_rate}")
    print(f"Final solution is {bin_epsilon_rate*bin_gamma_rate}")
