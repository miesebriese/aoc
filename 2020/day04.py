import re

pp_strings = [x.replace('\n', ' ').split(' ') for x in open('inputs/day04.txt').read().split('\n\n')]
pp_tuples = [[tuple(x.split(':')) for x in passport] for passport in pp_strings]

req_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
check_val = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: x.endswith('cm') and 150 <= int(x[:-2]) <= 193 or x.endswith('in') and 59 <= int(x[:-2]) <= 76,
    'hcl': lambda x: re.match(r'#[0-9a-f]{6}', x) is not None,
    'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda x: len(x) == 9 and x.isnumeric(),
    'cid': lambda _: True
}

pp_valid_keys = list(filter(lambda pp: req_keys.issubset([f[0] for f in pp]), pp_tuples))
pp_valid_vals = list(filter(lambda pp: all(map(lambda f: check_val[f[0]](f[1]), pp)), pp_valid_keys))

print('### day4 ###')
print('part1:', len(pp_valid_keys))
print('part2:', len(pp_valid_vals))
