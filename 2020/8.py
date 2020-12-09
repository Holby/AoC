import requests
from secret import cookie

def get_input(day):
    response = requests.get('https://adventofcode.com/2020/day/{}/input'.format(day), headers={
        'cookie': cookie})
    return response.text.splitlines()


def run_code(in_data):
    i = 0
    acc = 0
    processed = [False] * (len(in_data) + 1)

    while not processed[i]:
        processed[i] = True
        if processed[-1]:
            return acc, True
        op, arg = in_data[i].split(' ')
        if op == 'acc':
            acc += int(arg)
            i += 1
        elif op == 'jmp':
            i += int(arg)
        else:
            i += 1
    return acc, False


if __name__ == '__main__':
    in_data = get_input(8)
    print('Solution 1: {}'.format(run_code(in_data)[0]))
    done = False
    for i, line in enumerate(in_data):
        in_data_mod = in_data.copy()
        if line.find('nop') >= 0:
            in_data_mod[i] = line.replace('nop', 'jmp')
            acc, done = run_code(in_data_mod)
        elif line.find('jmp') >= 0:
            in_data_mod[i] = line.replace('jmp', 'nop')
            acc, done = run_code(in_data_mod)
        if done:
            print('Solution 2: {}'.format(acc))
            break
