from aoc_tools import get_input
from time import perf_counter
import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000,
     formatter=dict(float=lambda x: "%.3g" % x))


def foldx(ary, index):
    f1 = np.split(ary, [index], axis=1)[0]
    f2 = np.split(ary, [index], axis=1)[1][:, 1:]
    f2 = np.flip(f2, axis=1)
    return f1 + f2


def foldy(ary, index):
    f1 = np.split(ary, [index], axis=0)[0]
    f2 = np.split(ary, [index], axis=0)[1][1:]
    f2 = np.flip(f2, axis=0)
    return f1 + f2


def part12(in_data):
    xs, ys = [], []
    for i, line in enumerate(in_data):
        if not line:
            break
        xs.append(int(line.split(',')[0]))
        ys.append(int(line.split(',')[1]))
    paper = np.zeros((max(ys)+2, max(xs)+1))
    for x, y in zip(xs, ys):
        paper[y][x] = 1
    folded = foldx(paper, 655)
    print(f"Part1: {np.count_nonzero(folded)}")
    folded = foldy(folded, 447)
    folded = foldx(folded, 327)
    folded = foldy(folded, 223)
    folded = foldx(folded, 163)
    folded = foldy(folded, 111)
    folded = foldx(folded, 81)
    folded = foldy(folded, 55)
    folded = foldx(folded, 40)
    folded = foldy(folded, 27)
    folded = foldy(folded, 13)
    folded = foldy(folded, 6)
    folded = np.where(folded > 0, 1, folded)
    print("Part2: ")
    for row in folded:
        print(np.array2string(row).replace(' ', '').replace('1', '#').replace('0', ' '))


if __name__ == '__main__':
    puzzle_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".splitlines()
    puzzle_input = get_input(13).splitlines()
    start = perf_counter()
    part12(puzzle_input)

    print(f"Total runtime: {perf_counter() - start}")
