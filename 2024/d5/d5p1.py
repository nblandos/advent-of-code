import os
from collections import defaultdict

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

section1 = True
rules = defaultdict(list)
mid_sum = 0


def check_correct_update(line):
    line = line.split(",")
    appeared = set()
    for num in line:
        for rule in rules[num]:
            if rule in appeared:
                return 0
        appeared.add(num)
    return line[len(line) // 2]


def add_rule(line):
    before, after = line.split("|")
    rules[before].append(after)


with open(file_path, "r") as file:
    for line in file:
        if line == "\n":
            section1 = False
            continue
        line = line.strip()
        if section1:
            add_rule(line)
        else:
            mid_sum += int(check_correct_update(line))
            
  
print(mid_sum)
