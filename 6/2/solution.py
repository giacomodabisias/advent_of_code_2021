from functools import lru_cache


INPUT_FILE = "input.txt"


def read_input() -> list[int]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
    return [int(num) for num in lines[0].strip().split(",")]

@lru_cache(None)
def get_population_count(population: int, days: int, status: int) -> int:
    if days == 0:
        return population
    if status == 0:
        current = get_population_count(population, days - 1, 6)
        new_born = get_population_count(population, days - 1, 8)
        return current + new_born
    return get_population_count(population, days - 1, status - 1)


if __name__ == "__main__":
    fishes = read_input()
    total = 0
    for fish in fishes:
        total += get_population_count(1, 256, fish)

    print(total)











