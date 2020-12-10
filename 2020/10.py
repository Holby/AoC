import requests
from secret import cookie
from collections import Counter
import functools


def get_input(day):
    response = requests.get('https://adventofcode.com/2020/day/{}/input'.format(day), headers={
        'cookie': cookie})
    return response.text.splitlines()


@functools.lru_cache(maxsize=None)
def find_adapt(adapters):
    if len(adapters) == 1:
        return 1
    ret = 0
    for i in range(1, len(adapters)):
        ret += find_adapt(adapters[i:]) if adapters[i] - adapters[0] < 4 else 0
    return ret


if __name__ == '__main__':
    in_data = sorted([int(line) for line in get_input(10)] + [0])
    in_data.append(in_data[-1] + 3)
    res = Counter([a - b for a, b in zip(in_data, [0] + in_data)])

    print('Solution 1: {}'.format(res[1] * res[3]))
    print('Solution 2: {}'.format(find_adapt(tuple(in_data))))

