from aoc_tools import get_input
from time import perf_counter
from itertools import count
import numpy as np


def part12(el):
    flashes = 0
    for step in count(1):
        el += 1
        while np.where(el > 9)[0].any():
            for y, x in zip(np.where(el > 9)[0], np.where(el > 9)[1]):
                el[y - 1:y + 2, x - 1:x + 2] += 1
                el[y][x] = -100
                flashes += 1
        el[1:-1, 1:-1] = np.where(el[1:-1, 1:-1] < 0, 0, el[1:-1, 1:-1])
        if step == 100:
            print(f"Part 1: {flashes}")
        if np.all((el[1:-1, 1:-1]) == 0):
            print(f"Part 2: {step}")
            return


if __name__ == '__main__':
    puzzle_input = " ".join("""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""").splitlines()
    puzzle_input = " ".join(get_input(11)).splitlines()
    el = np.loadtxt(puzzle_input, int)
    border_val = -np.inf
    el = np.c_[np.ones(len(el), int) * border_val, el, np.ones(len(el), int) * border_val]
    el = np.vstack([np.ones(len(el[0]), int) * border_val, el, np.ones(len(el[0]), int) * border_val])
    start = perf_counter()
    part12(el)
    print(f"Total runtime: {perf_counter() - start}")
