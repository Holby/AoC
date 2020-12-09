import requests
import cProfile
from secret import cookie

def get_input(day):
    response = requests.get('https://adventofcode.com/2020/day/{}/input'.format(day), headers={
        'cookie': cookie})
    return response.text.rstrip().split('\n\n')


def dict_sol(in_data):
    # Using dict
    sum1 = 0
    sum2 = 0
    for batch in in_data:
        d = dict.fromkeys(list(batch + '\n'), 0)
        sum1 += len(list(d)) - 1
        for letter in list(batch):
            d[letter] += 1
        sum2 += len([val for val in d.values() if val == d['\n'] + 1])
    print('Solution 1: {}'.format(sum1))
    print('Solution 2: {}'.format(sum2))


def set_sol(in_data):
    # Using set
    sum1 = 0
    sum2 = 0
    for batch in in_data:
        l = batch.split('\n')
        sum1 += len(set.union(*map(set, l)))
        sum2 += len(set.intersection(*map(set, l)))
    print('Solution 1: {}'.format(sum1))
    print('Solution 2: {}'.format(sum2))



if __name__ == '__main__':
    in_data = get_input(6)
    cProfile.run('dict_sol(in_data)')
    cProfile.run('set_sol(in_data)')