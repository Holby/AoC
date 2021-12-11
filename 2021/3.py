from aoc_tools import get_input
from time import perf_counter
import numpy as np


def part1(in_data):
    m = [list(x) for x in in_data]
    b_array = np.array(m).astype(int).mean(axis=0).round().astype(int).tolist()
    b_str = ""
    b_str_inv = ""
    d = {'1': '0', '0': '1'}
    for num in map(str, b_array):
        b_str += num
        b_str_inv += d[num]
    return int(b_str, 2) * int(b_str_inv, 2)


def part2(in_data):
    m = [list(x) for x in in_data]
    m2 = m
    for i, _ in enumerate(m[0]):
        avg = np.array(m).astype(int).mean(axis=0)[i]
        if avg >= 0.5:
            m = [x for x in m if x[i] == '1']
        else:
            m = [x for x in m if x[i] == '0']
        if len(m) == 1:
            oxy = int(''.join(m[0]), 2)
            break
    m = m2
    for i, _ in enumerate(m[0]):
        avg = np.array(m).astype(int).mean(axis=0)[i]
        if avg >= 0.5:
            m = [x for x in m if x[i] == '0']
        else:
            m = [x for x in m if x[i] == '1']
        if len(m) == 1:
            co2 = int(''.join(m[0]), 2)
            break
    return oxy * co2

if __name__ == '__main__':
    puzzle_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".splitlines()
    puzzle_input = get_input(3).splitlines()
    start = perf_counter()

    print(f"Part 1: {part1(puzzle_input)}, time: {perf_counter()-start}")
    start2 = perf_counter()
    print(f"Part 2: {part2(puzzle_input)}, time: {perf_counter()-start2}")

    print(f"Total runtime: {perf_counter()-start}")
