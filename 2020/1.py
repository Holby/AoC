import requests
from secret import cookie

headers = {
    'cookie': cookie,
}

response = requests.get('https://adventofcode.com/2020/day/1/input', headers=headers)

in_data = response.text.split('\n')[:-1]
in_data=[int(x) for x in in_data]

target_sum = 2020
seen = [False] * target_sum

for term in in_data:
    if seen[target_sum - term]:
        print('Solution 1: {}'.format((target_sum - term)*term))
    else:
        seen[term] = True

hash_tbl = [False] * (target_sum + 1)
sorted_input = sorted(in_data)
for a in sorted_input:
    for b in sorted_input:
        if a + b <= target_sum:
            hash_tbl[a+b] = a*b
        else:
            break

for c in sorted_input:
    if ab := hash_tbl[target_sum - c]:
        print('Solution 2: {}'.format((ab*c)))
        break
