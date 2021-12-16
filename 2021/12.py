from aoc_tools import get_input
from time import perf_counter


def f1(path):
    global caves
    ways = caves[path[-1]]
    res = 0
    for way in ways:
        if way == 'start':
            continue
        if way == 'end':
            res += 1
            continue
        if way.isupper():
            res += f1(path+(way,))
        if way.islower():
            if way not in path:
                res += f1(path + (way,))
    return res


def f2(path):
    global caves
    res = 0
    ways = caves[path[-1]]
    for way in ways:
        if way == 'start':
            continue
        if way == 'end':
            res += 1
            continue
        if way.isupper():
            res += f2(path+(way,))
        if way.islower():
            lower = [x for x in path if x.islower()]
            if way not in path or len(lower) == len(set(lower)):
                res += f2(path + (way,))
    return res


if __name__ == '__main__':
    puzzle_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".splitlines()
    puzzle_input = get_input(12).splitlines()
    caves = {}
    for line in puzzle_input:
        caves[line.split('-')[0]] = []
        caves[line.split('-')[1]] = []
    for line in puzzle_input:
        caves[line.split('-')[0]].append(line.split('-')[1])
        caves[line.split('-')[1]].append(line.split('-')[0])

    start = perf_counter()
    print(f"Part 1: {f1(('start',))}, time: {perf_counter()-start}")
    start2 = perf_counter()

    print(f"Part 2: {f2(('start',))}, time: {perf_counter() - start2}")
    print(f"Total runtime: {perf_counter() - start}")
