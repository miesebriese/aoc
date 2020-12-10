import re

rules = open('inputs/day07.txt').read().splitlines()
bag_pattern = re.compile(r'(\d+) (\w+ \w+) bag')
rule_dict = {}

for rule in rules:
    matches = bag_pattern.findall(rule)
    contains = {}
    for count, color in matches:
        contains[color] = int(count)
    rule_dict[' '.join(rule.split(' ')[:2])] = contains


def find_parents(bag_color):
    parents = set()
    for parent, children in rule_dict.items():
        for child in children:
            if bag_color == child:
                parents |= ({parent} | find_parents(parent))
    return parents


def count_children(bag_color):
    children = 0
    for child_color, child_count in rule_dict[bag_color].items():
        children += child_count + child_count * count_children(child_color)
    return children


print('### day7 ###')
print('part1:', len(find_parents('shiny gold')))
print('part2:', count_children("shiny gold"))
