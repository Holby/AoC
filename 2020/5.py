import requests
from secret import cookie

def get_input(day):
    response = requests.get('https://adventofcode.com/2020/day/{}/input'.format(day), headers={
    'cookie': cookie})
    return response.text.splitlines()


def get_id(bp):
    bp = bp.replace('R', 'B').replace('B', '1')
    bp = bp.replace('L', 'F').replace('F', '0')
    return int(bp, 2)


if __name__ == '__main__':
    in_data = get_input(5)
    ids = []
    for bp in in_data:
        ids.append(get_id(bp))

    print('Solution 1: {}'.format(max(ids)))
    print('Solution 2: {}'.format(list(set(range(min(ids), max(ids), 1)) - set(ids))[0]))
