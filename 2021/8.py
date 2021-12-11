from aoc_tools import get_input
from time import perf_counter


def part1(in_data):
    unique = 0
    for line in in_data:
        output = line.split('|')[1].split(' ')[1:]
        for val in output:
            if len(val) in [2, 3, 4, 7]:
                unique += 1
    return unique


def part2(in_data):
    out_sum = 0
    for line in in_data:
        locked = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
        segs = {}
        possible = line.split('|')[0].split(' ')[:-1]
        len6 = []
        for val in possible:
            if len(val) == 2:
                locked[1] = val
            if len(val) == 3:
                locked[7] = val
            if len(val) == 4:
                locked[4] = val
            if len(val) == 6:
                len6.append(val)
            if len(val) == 7:
                locked[8] = val
        segs['a'] = locked[7]
        for char in locked[1]:
            segs['a'] = segs['a'].replace(char, "")
        for val in len6:
            if set(locked[4]).issubset(set(val)):
                locked[9] = val
                len6.remove(val)
        for val in len6:
            if set(locked[1]).issubset(set(val)):
                locked[0] = val
                len6.remove(val)
        locked[6] = len6[0]
        segs['d'] = locked[8]
        for char in locked[0]:
            segs['d'] = segs['d'].replace(char, "")

        segs['c'] = locked[8]
        for char in locked[6]:
            segs['c'] = segs['c'].replace(char, "")

        segs['e'] = locked[8]
        for char in locked[9]:
            segs['e'] = segs['e'].replace(char, "")

        if locked[1][0] in segs.values():
            segs['f'] = locked[1][1]
        else:
            segs['f'] = locked[1][0]

        for i in locked[4]:
            if i not in segs.values():
                segs['b'] = i

        last = "abcdefg"
        for char in "".join(segs.values()):
            last = last.replace(char, "")
        segs['g'] = last
        segs = {ord(v): k for (k, v) in segs.items()}
        num_map = {"abcefg": '0', "cf": '1', "acdeg": '2', "acdfg": '3', "bcdf": '4', "abdfg": '5', "abdefg": '6', "acf": '7', "abcdefg": '8', "abcdfg": '9'}
        output = line.split('|')[1].split(' ')[1:]
        out_str = ""
        for val in output:
            out_str += num_map["".join(sorted(val.translate(segs)))]
        out_sum += int(out_str)
    return out_sum


if __name__ == '__main__':
    puzzle_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".splitlines()
    puzzle_input = get_input(8).splitlines()
    start = perf_counter()
    print(f"Part 1: {part1(puzzle_input)}, time: {perf_counter()-start}")
    start2 = perf_counter()
    print(f"Part 2: {part2(puzzle_input)}, time: {perf_counter() - start2}")
    print(f"Total runtime: {perf_counter() - start}")
