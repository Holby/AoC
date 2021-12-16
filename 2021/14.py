from aoc_tools import get_input
from time import perf_counter


def part12(in_data, steps):
    template = in_data[0]
    inst = {}
    for line in in_data[2:]:
        inst[line.split(' -> ')[0]] = line.split(' -> ')[1]
    pol_cnt = {}
    for i in range(len(template)-1):
        pol_cnt[template[i:i + 2]] = pol_cnt.get(template[i:i+2], 0) + 1

    for step in range(0, steps):
        tmp = {}
        for k in pol_cnt.keys():
            a, b = k[0]+inst[k], inst[k] + k[1]
            tmp[a] = tmp.get(a, 0) + pol_cnt.get(k, 1)
            tmp[b] = tmp.get(b, 0) + pol_cnt.get(k, 1)
        pol_cnt = tmp

    d = {template[-1]: 1, template[0]: 1}
    for k, v in pol_cnt.items():
        d[k[0]] = d.get(k[0], 0) + v
        d[k[1]] = d.get(k[1], 0) + v

    return max(d.values())/2 - min(d.values())/2

if __name__ == '__main__':
    puzzle_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".splitlines()
    puzzle_input = get_input(14).splitlines()
    start = perf_counter()
    print(f"Part 1: {part12(puzzle_input, 10)}, time: {perf_counter()-start}")
    start2 = perf_counter()
    print(f"Part 2: {part12(puzzle_input, 40)}, time: {perf_counter() - start2}")
    print(f"Total runtime: {perf_counter() - start}")
