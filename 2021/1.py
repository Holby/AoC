from aoc_tools import get_input
from time import perf_counter


def part1(input):
    cnt = 0
    for d1, d2 in zip(input, input[1:]):
        if int(d1) < int(d2):
            cnt += 1
    return cnt


def part2(input):
    l = []
    for d1, d2, d3 in zip(input, input[1:], input[2:]):
        s = int(d1)+int(d2)+int(d3)
        l.append(s)
    return part1(l)


if __name__ == '__main__':

    puzzle_input = get_input(1).splitlines()
    start = perf_counter()

    print(f"Part 1: {part1(puzzle_input)}, time: {perf_counter()-start}")
    start2 = perf_counter()
    print(f"Part 2: {part2(puzzle_input)}, time: {perf_counter()-start2}")

    print(f"Total runtime: {perf_counter()-start}")
