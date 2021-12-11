from aoc_tools import get_input
from time import perf_counter
import numpy as np


def part1(in_data):
    open_chars = "([{<"
    matching = {'(': ')', '[': ']', '{': '}', '<': '>'}
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    res = 0
    for line in in_data:
        stack = []
        for char in line:
            if char in open_chars:
                stack.append(matching[char])
            else:
                if stack.pop() != char:
                    res += points[char]
    return res


def part2(in_data):
    open_chars = "([{<"
    matching = {'(': ')', '[': ']', '{': '}', '<': '>'}
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    res = []
    for line in in_data:
        stack = []
        for i, char in enumerate(line):
            if char in open_chars:
                stack.append(matching[char])
            else:
                if stack.pop() != char:
                    break
            if i == len(line) - 1:
                line_res = 0
                for c in reversed(stack):
                    line_res = line_res*5 + points[c]
                res.append(line_res)
    return int(np.median(res))


if __name__ == '__main__':
    puzzle_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".splitlines()
    puzzle_input = get_input(10).splitlines()
    start = perf_counter()
    print(f"Part 1: {part1(puzzle_input)}, time: {perf_counter()-start}")
    start2 = perf_counter()
    print(f"Part 2: {part2(puzzle_input)}, time: {perf_counter() - start2}")
    print(f"Total runtime: {perf_counter() - start}")
