from functools import reduce

group_answers = open('inputs/day06.txt').read().split('\n\n')
answer_sets = [[set(x) for x in answer] for answer in [x.split('\n') for x in group_answers]]

print('### day6 ###')
print('part1:', sum(map(len, [reduce(lambda x, y: x | y, a) for a in answer_sets])))
print('part2:', sum(map(len, [reduce(lambda x, y: x & y, a) for a in answer_sets])))
