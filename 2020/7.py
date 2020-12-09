import requests
import re
from secret import cookie

def get_input(day):
    response = requests.get('https://adventofcode.com/2020/day/{}/input'.format(day), headers={
        'cookie': cookie})
    return response.text


def part1(bag_name, in_data):
    l = []
    for rule in in_data:
        if rule.find(' ' + bag_name) >= 0:
            l.append(rule[:rule.find(' bags')])
            l = l + part1(rule[:rule.find(' bags')], in_data)
    return l


def part2(bag_name, in_data):
    ret = 0
    if rule := re.findall("(\n{}.*[0-9].*)".format(bag_name), in_data):
        for i in re.findall("([0-9]+ )(.*?)(?= bag)", rule[0]):
            ret += int(i[0]) + int(i[0]) * part2(i[1], in_data)
    return ret

# def part2(bag_name, in_data):
#     ret = 0
#     for rule in in_data:
#         if re.findall("^{}.*[0-9]".format(bag_name), rule):
#             for i in re.findall("([0-9]+ )(.*?)(?= bag)", rule):
#                 ret += int(i[0]) + int(i[0]) * part2(i[1], in_data)
#             return ret
#     return 0


if __name__ == '__main__':
    in_data = get_input(7)
    print('Solution 1: {}'.format(len(dict.fromkeys(part1('shiny gold', in_data.splitlines())))))
    print('Solution 2: {}'.format(part2('shiny gold', in_data)))