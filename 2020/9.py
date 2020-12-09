import requests
from secret import cookie

def get_input(day):
    response = requests.get('https://adventofcode.com/2020/day/{}/input'.format(day), headers={
        'cookie': cookie})
    return response.text.splitlines()


def get_valid(pre):
    valid = []
    for i in range(0, len(pre)):
        for j in range(0, len(pre)):
            if i != j:
                valid.append(pre[i] + pre[j])
    return valid


def part1(in_data):
    pre_size = 25
    for i, num in enumerate(in_data):
        if i > pre_size - 1:
            valid = get_valid(in_data[i - pre_size:i])
            if num not in valid:
                return num


def part2(in_data, target):
    for j in range(0, len(in_data)):
        s = in_data[j]
        i = j
        while s < target:
            i += 1
            s += in_data[i]
        if s == target:
            return min(in_data[j:i+1]) + max(in_data[j:i+1])


if __name__ == '__main__':
    in_data = [int(line) for line in get_input(9)]
    ans1 = part1(in_data)

    print('Solution 1: {}'.format(ans1))
    print('Solution 2: {}'.format(part2(in_data, ans1)))
