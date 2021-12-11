from aoc_tools import get_input
from time import perf_counter
import numpy as np
from skimage.draw import line


def part1(in_data):
    ocean_floor = np.zeros((1000, 1000))
    for l in in_data:
        x1, y1, x2, y2 = map(int, l.replace(" -> ", ',').split(','))
        if x1 == x2 or y1 == y2:
            ocean_floor[min(y1, y2):max(y1, y2) + 1, min(x1, x2):max(x1, x2) + 1] += 1
    return np.count_nonzero(np.where(ocean_floor < 2, 0, ocean_floor))


def part2(in_data):
    ocean_floor = np.zeros((1000, 1000))
    for l in in_data:
        ocean_floor[line(*map(int, l.replace(" -> ", ',').split(',')))] += 1
    return np.count_nonzero(np.where(ocean_floor < 2, 0, ocean_floor))


if __name__ == '__main__':
    puzzle_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".splitlines()
    puzzle_input = get_input(5).splitlines()
    start = perf_counter()

    print(f"Part 1: {part1(puzzle_input)}, time: {perf_counter()-start}")
    start2 = perf_counter()
    print(f"Part 2: {part2(puzzle_input)}, time: {perf_counter()-start2}")
    print(f"Total runtime: {perf_counter()-start}")