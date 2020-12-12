import requests
from secret import cookie
from copy import deepcopy


def get_input(day):
    response = requests.get('https://adventofcode.com/2020/day/{}/input'.format(day), headers={
        'cookie': cookie})
    return response.text.splitlines()


def part1(in_data):
    pos = [0, 0]
    rot = 0
    for line in in_data:
        dir = line[:1]
        steps = int(line[1:])
        if dir == 'E' or (dir == 'F' and rot == 0):
            pos[0] += steps
        elif dir == 'S' or (dir == 'F' and rot == 1):
            pos[1] -= steps
        elif dir == 'W' or (dir == 'F' and rot == 2):
            pos[0] -= steps
        elif dir == 'N' or (dir == 'F' and rot == 3):
            pos[1] += steps
        elif dir == 'R':
            rot += steps / 90
        else:
            rot -= steps / 90
        rot %= 4
    return abs(pos[0]) + abs(pos[1])


def part2(in_data):
    pos = [0, 0]
    wp = [10, 1]
    for line in in_data:
        dir = line[:1]
        steps = int(line[1:])
        if dir == 'E':
            wp[0] += steps
        elif dir == 'S':
            wp[1] -= steps
        elif dir == 'W':
            wp[0] -= steps
        elif dir == 'N':
            wp[1] += steps
        elif dir == 'R':
            for i in range(int(steps / 90)):
                wp = [wp[1], wp[0] * -1]
        elif dir == 'L':
            for i in range(int(steps / 90)):
                wp = [wp[1] * -1, wp[0]]
        else:
            pos[0] += wp[0] * steps
            pos[1] += wp[1] * steps
    return abs(pos[0]) + abs(pos[1])


if __name__ == '__main__':
    in_data = get_input(12)
    print('Solution 1: {}'.format(part1(in_data)))
    print('Solution 2: {}'.format(part2(in_data)))
