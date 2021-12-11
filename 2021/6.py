from aoc_tools import get_input
from time import perf_counter
import numpy as np
from collections import Counter


def part1(in_data):
    fish = np.loadtxt(in_data, int, delimiter=',')
    for j in range(0, 80):
        for i in range(0, np.count_nonzero(fish == 0)):
            fish = np.concatenate((fish, [9]))
        fish = np.where(fish == 0, 7, fish)
        fish -= 1
    return len(fish)


def part2(in_data):
    fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    fish.update(Counter(np.loadtxt(in_data, int, delimiter=',')))
    for j in range(0, 256):
        new_fish = fish[0]
        for i in range(0, 8):
            fish[i] = fish[i + 1]
        fish[8] = new_fish
        fish[6] += new_fish

    return sum(fish.values())


if __name__ == '__main__':
    puzzle_input = """3,4,3,1,2""".splitlines()
    puzzle_input = get_input(6).splitlines()
    start = perf_counter()
    print(f"Part 1: {part1(puzzle_input)}, time: {perf_counter()-start}")
    start2 = perf_counter()
    print(f"Part 2: {part2(puzzle_input)}, time: {perf_counter() - start2}")
    print(f"Total runtime: {perf_counter() - start}")
