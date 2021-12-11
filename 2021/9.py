from aoc_tools import get_input
from time import perf_counter
import numpy as np


def part1(hm):
    rl = []
    for x in range(1, len(hm[0])-1):
        for y in range(1, len(hm) - 1):
            if hm[y-1][x] > hm[y][x] and hm[y+1][x] > hm[y][x] and hm[y][x-1] > hm[y][x] and hm[y][x+1] > hm[y][x]:
                rl.append(hm[y][x]+1)
    return sum(rl)


def bas_size(hm, x, y, res):
    hm[y][x] = False
    if hm[y][x+1]:
        res = bas_size(hm, x + 1, y, res)
    if hm[y+1][x]:
        res = bas_size(hm, x, y + 1, res)
    if hm[y][x-1]:
        res = bas_size(hm, x - 1, y, res)
    if hm[y-1][x]:
        res = bas_size(hm, x, y - 1, res)
    return res + 1


def part2(hm):
    hm = np.where(hm != 9, True, hm)
    hm = np.where(hm == 9, False, hm)
    lens = []
    while np.nonzero(hm)[0].any():
        lens.append(bas_size(hm, np.nonzero(hm)[1][0], np.nonzero(hm)[0][0], 0))

    return np.prod(sorted(lens)[-3:])


if __name__ == '__main__':
    puzzle_input = " ".join("""2199943210
3987894921
9856789892
8767896789
9899965678""").splitlines()
    puzzle_input = " ".join(get_input(9)).splitlines()
    hm = np.loadtxt(puzzle_input, int)
    hm = np.c_[np.ones(len(hm), int) * 9, hm, np.ones(len(hm), int) * 9]
    hm = np.vstack([np.ones(len(hm[0]), int) * 9, hm, np.ones(len(hm[0]), int) * 9])
    start = perf_counter()
    print(f"Part 1: {part1(hm)}, time: {perf_counter()-start}")
    start2 = perf_counter()
    print(f"Part 2: {part2(hm)}, time: {perf_counter() - start2}")
    print(f"Total runtime: {perf_counter() - start}")
