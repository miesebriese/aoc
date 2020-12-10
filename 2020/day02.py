import re

pw_pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
lines = [x for x in open('inputs/day02.txt')]
matched = [pw_pattern.match(line).groups() for line in lines]


def policy1(x):
    return int(x[0]) <= x[3].count(x[2]) <= int(x[1])


def policy2(x):
    return (x[3][int(x[0]) - 1] == x[2]) != (x[3][int(x[1]) - 1] == x[2])


print('### day2 ###')
print('part1:', len(list(filter(policy1, matched))))
print('part2:', len(list(filter(policy2, matched))))
