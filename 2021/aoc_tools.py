import requests
import requests_cache
from secret import cookie

requests_cache.install_cache('input_cache')


def get_input(day):
    response = requests.get('https://adventofcode.com/2021/day/{}/input'.format(day), headers={
        'cookie': cookie})
    return response.text


def print_res(res1, res2):
    pass