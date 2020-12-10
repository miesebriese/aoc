from itertools import combinations
from math import prod

lines = [int(x) for x in open('inputs/day01.txt')]
year = 2020


def solve(length):
    return prod(next(filter(lambda x: sum(x) == year, combinations(lines, length))))


print('### day2 ###')
print('part1:', solve(2))
print('part1:', solve(3))
