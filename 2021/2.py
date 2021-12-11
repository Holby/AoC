from aoc_tools import get_input
from time import perf_counter


def part1(input):
    x = 0
    y = 0
    for line in input:
        direction, amount = line.split(' ')
        if direction == 'forward':
            x += int(amount)
        elif direction == 'down':
            y += int(amount)
        else:  # up
            y -= int(amount)
    return x * y


def part2(input):
    x = 0
    y = 0
    aim = 0
    for line in input:
        direction, amount = line.split(' ')
        if direction == 'forward':
            x += int(amount)
            y += int(amount) * aim
        elif direction == 'down':
            aim += int(amount)
        else:  # up
            aim -= int(amount)
    return x * y


if __name__ == '__main__':
    puzzle_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()
    puzzle_input = get_input(2).splitlines()
    start = perf_counter()

    print(f"Part 1: {part1(puzzle_input)}, time: {perf_counter()-start}")
    start2 = perf_counter()
    print(f"Part 2: {part2(puzzle_input)}, time: {perf_counter()-start2}")

    print(f"Total runtime: {perf_counter()-start}")
