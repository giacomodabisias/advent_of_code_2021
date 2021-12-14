
INPUT_FILE = "input.txt"


digits_to_len = {"2": 1, "4": 4, "3": 7, "7": 8}

def read_input() -> tuple[list[list[str]], list[list[str]]]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
    outputs = []
    inputs = []
    for line in lines:
        new_outputs = []
        new_inputs = []
        output_words = line.strip().split("|")[1]
        input_words = line.strip().split("|")[0]
        for word in output_words.split(" "):
            if len(word) > 0:
                new_outputs.append(word)
        for word in input_words.split(" "):
            if len(word) > 0:
                new_inputs.append(word)
        outputs.append(new_outputs)
        inputs.append(new_outputs)
    return inputs, outputs


if __name__ == "__main__":
    inputs, outputs = read_input()
    total_unique_words = 0
    for output in outputs:
        for word in output:
            if str(len(word)) in digits_to_len:
                total_unique_words += 1
    print(total_unique_words)











