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
                return order_line(line)[len(line) // 2]
        appeared.add(num)
    return 0


def order_line(line):
    appeared = set()
    num_set = set(line)
    ordered_line = []
   
    def visit(num):
        if num in appeared:
            return
        appeared.add(num)
        for rule in rules[num]:
            if rule in num_set:
                visit(rule)
        ordered_line.append(num)
       
    for num in line:
        visit(num)
           
    return ordered_line[::-1]


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
