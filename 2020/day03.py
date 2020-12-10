from math import prod

lines = [x.strip() for x in open('inputs/day03.txt')]
line_width = len(lines[0])


def count_trees(slope_right, slope_down):
    trees = x = y = 0
    while y < len(lines):
        if lines[y][x % line_width] == '#':
            trees += 1
        x += slope_right
        y += slope_down
    return trees


print('### day3 ###')
print('part1:', count_trees(3, 1))
print('part2:', prod([count_trees(x[0], x[1]) for x in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]))
