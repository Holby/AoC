import requests
import copy
import re
from secret import cookie

headers = {
    'cookie': cookie,
}

response = requests.get('https://adventofcode.com/2020/day/4/input', headers=headers)

in_data = response.text.split('\n\n')[:-1]

template = {
    'byr' : None,
    'iyr' : None,
    'eyr' : None,
    'hgt' : None,
    'hcl' : None,
    'ecl' : None,
    'pid' : None,
    'cid' : '1337'
}

def validate(tmp):
    return re.search("^19[2-9][0-9]|200[0-2]$", tmp['byr'])\
           and re.search("^201[0-9]|2020$", tmp['iyr'])\
           and re.search("^202[0-9]|2030$", tmp['eyr'])\
           and re.search("^#[0-9a-f]{6}$", tmp['hcl'])\
           and re.search("amb|blu|brn|gry|grn|hzl|oth", tmp['ecl'])\
           and re.search("^[0-9]{9}$", tmp['pid'])\
           and re.search("^(59|6[0-9]|7[0-6])in$|^(1[5-8][0-9]|19[0-3])cm$",tmp['hgt'])

valid = 0
valid2 = 0
for passp in in_data:
    tmp = copy.deepcopy(template)
    for field in passp.replace('\n',' ').split(' '):
        pair = field.split(':')
        tmp[pair[0]] = pair[1]
    if all(tmp.values()) :
        valid += 1
        if validate(tmp):
            valid2 += 1

print('Solution 1: {}'.format(valid))
print('Solution 2: {}'.format(valid2))
