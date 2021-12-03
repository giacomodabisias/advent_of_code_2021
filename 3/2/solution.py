INPUT_FILE = "input.txt"


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


def remove_nums(idx, nums, most_significant):
    if len(nums) == 1:
        return nums[0]
    else:
        ones = 0
        zeros = 0
        for num in nums:
            if num[idx] == "0":
                zeros += 1
            else:
                ones += 1
        if most_significant:
            most_common = "0" if zeros > ones else "1"
        else:
            most_common = "1" if zeros > ones else "0"

        new_nums = [num for num in nums if num[idx] == most_common]
        idx += 1
        return remove_nums(idx, new_nums, most_significant)


if __name__ == "__main__":
    bins = read_input()
    values = []

    oxygen_generator_rating = remove_nums(idx=0, nums=bins, most_significant=True)
    bin_oxygen_generator_rating = to_bin(oxygen_generator_rating)
    print(f"Oxygen generator rating: {bin_oxygen_generator_rating}")

    co2_scrubber_rating = remove_nums(idx=0, nums=bins, most_significant=False)
    bin_co2_scrubber_rating = to_bin(co2_scrubber_rating)
    print(f"Co2 scrubber rating: {bin_co2_scrubber_rating}")

    print(f"Final result {bin_oxygen_generator_rating*bin_co2_scrubber_rating}")
