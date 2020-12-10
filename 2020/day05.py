lines = open('inputs/day05.txt').read().splitlines()
ids = [int(line.translate({70: 48, 66: 49, 76: 48, 82: 49}), 2) for line in lines]

print('### day5 ###')
print('part1:', max(ids))
print('part2:', next(filter(lambda x: x not in ids, range(min(ids), max(ids)))))
