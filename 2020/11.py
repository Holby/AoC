import requests
from secret import cookie
from copy import deepcopy


def get_input(day):
    response = requests.get('https://adventofcode.com/2020/day/{}/input'.format(day), headers={
        'cookie': cookie})
    return response.text.splitlines()


def part1(in_data):
    next_frame = [['0'] * (len(in_data[1]) + 2)]
    frame = []
    for line in in_data:
        next_frame.append(['0'] + list(line) + ['0'])
    next_frame.append(['0'] * (len(in_data[1]) + 2))
    while frame != next_frame:
        frame = deepcopy(next_frame)
        for i in range(1, len(frame) - 1):
            for j in range(1, len(frame[1]) - 1):
                if frame[i][j] == '.':
                    continue
                adj = []
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if k == 0 and l == 0:
                            continue
                        adj.append(frame[i + k][j + l])
                if frame[i][j] == 'L' and '#' not in adj:
                    next_frame[i][j] = '#'
                elif frame[i][j] == '#' and adj.count('#') > 3:
                    next_frame[i][j] = 'L'
    return next_frame


def part2(in_data):
    next_frame = [['0'] * (len(in_data[1]) + 2)]
    frame = []
    for line in in_data:
        next_frame.append(['0'] + list(line) + ['0'])
    next_frame.append(['0'] * (len(in_data[1]) + 2))
    while frame != next_frame:
        frame = deepcopy(next_frame)
        for i in range(1, len(frame) - 1):
            for j in range(1, len(frame[1]) - 1):
                if frame[i][j] == '.':
                    continue
                adj = []
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if k == 0 and l == 0:
                            continue
                        x = 1
                        while frame[i + k*x][j + l*x] == '.':
                            x += 1
                        adj.append(frame[i + k*x][j + l*x])
                if frame[i][j] == 'L' and '#' not in adj:
                    next_frame[i][j] = '#'
                elif frame[i][j] == '#' and adj.count('#') > 4:
                    next_frame[i][j] = 'L'
    return next_frame


if __name__ == '__main__':
    in_data = get_input(11)
    res1 = 0
    res2 = 0
    for row in part1(in_data):
        res1 += row.count('#')
    print('Solution 1: {}'.format(res1))
    for row in part2(in_data):
        res2 += row.count('#')
    print('Solution 2: {}'.format(res2))
