import requests
from secret import cookie

headers = {
    'cookie': cookie,
}

response = requests.get('https://adventofcode.com/2020/day/3/input', headers=headers)

in_data = response.text.split('\n')[:-1]

map = []

for line in in_data:
    map.append(list(line))

xlim = len(map[0])
ylim = len(map)-1
x = 0
y = 0
trees = 0

while y < ylim :
    x += 3
    y += 1
    if map[y][x % xlim] == '#':
        trees += 1

print('Solution 1: {}'.format(trees))
slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]

tot = 1
for slope in slopes:
    x = 0
    y = 0
    trees = 0
    while y < ylim :
        x += slope[1]
        y += slope[0]
        if map[y][x % xlim] == '#':
            trees += 1
    tot = tot * trees
print('Solution 2: {}'.format(tot))