from aoc_tools import get_input
from time import perf_counter
import numpy as np


def part12(in_data):
    first = True
    numbers = in_data[0].split(',')
    boards = np.loadtxt(in_data[1:], int).reshape(-1, 5, 5)
    for in_num in map(int, numbers):
        to_delete = []
        for i, board in enumerate(boards):
            boards[i] = np.where(board == in_num, -1, board)
            if -5 in board.sum(axis=1) or -5 in board.sum(axis=0):
                if first:
                    first = False
                    print(f"part1: {np.where(board == -1, 0, board).sum() * in_num}")
                if len(boards) == 1:
                    print(f"part2: {np.where(board == -1, 0, board).sum() * in_num}")
                    return
                to_delete.append(i)
        boards = np.delete(boards, to_delete, 0)


if __name__ == '__main__':
    puzzle_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".splitlines()
    puzzle_input = get_input(4).splitlines()

    start = perf_counter()
    part12(puzzle_input)
    print(f"Total runtime: {perf_counter()-start}")
