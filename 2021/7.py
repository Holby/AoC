from aoc_tools import get_input
from time import perf_counter
import numpy as np


def part1(in_data):
    crabs = np.loadtxt(in_data, int, delimiter=',')
    return np.abs(crabs - np.median(crabs)).sum()


def part2(in_data):
    crabs = np.loadtxt(in_data, int, delimiter=',')
    last_fuel = np.inf
    v_get_fuel = np.vectorize(lambda d: d*(d+1)/2)
    for i in range(0, max(crabs)):
        fuel = (v_get_fuel(np.abs(crabs - i))).sum()
        if fuel > last_fuel:
            return last_fuel
        last_fuel = fuel


def part3(in_data):
    # After realizing mean ~ optimal...
    crabs = np.loadtxt(in_data, int, delimiter=',')
    v_get_fuel = np.vectorize(lambda d: d * (d + 1) / 2)
    return (v_get_fuel(np.abs(crabs - np.floor(np.mean(crabs))))).sum()


if __name__ == '__main__':
    puzzle_input = """16,1,2,0,4,2,7,1,2,14""".splitlines()
    puzzle_input = get_input(7).splitlines()
    start = perf_counter()
    print(f"Part 1: {part1(puzzle_input)}, time: {perf_counter()-start}")
    start2 = perf_counter()
    print(f"Part 2: {part2(puzzle_input)}, time: {perf_counter() - start2}")
    start2 = perf_counter()
    print(f"Part 3: {part3(puzzle_input)}, time: {perf_counter() - start2}")
    print(f"Total runtime: {perf_counter() - start}")